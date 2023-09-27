import inspect
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
from mendeley import Mendeley
import time

def get_mendeley_session(ID, SECRET, AUTH_URI, STATE):
    mendeley = Mendeley(ID, SECRET, redirect_uri=AUTH_URI)
    auth = mendeley.start_authorization_code_flow(state=STATE)
    session = auth.authenticate(
    f'{AUTH_URI}?code={st.session_state["token"]["code"][0]}&state={st.session_state["token"]["state"][0]}'
    )
    
    return session

def download_file(session, file_id, file_path="tmp.pdf"):
    rsp = session.get(f"https://api.mendeley.com/files/{file_id}", stream=True)
    with open(file_path, 'wb') as f:
        for block in rsp.iter_content(1024):
            if not block:
                break
            f.write(block)
    
    return file_path

# Header
cookies = EncryptedCookieManager(password='insaneSBL', expiration_seconds=60)
if not cookies.ready():
    st.stop()

REDIRECT_URI = 'http://localhost:5000/oauth'
MENDELEY_URI = 'https://api.mendeley.com'
# Main
st.sidebar.markdown(
    """
    Summarise scientific paper with AI.     
    Author: sanekun@kaist.ac.kr  
    
    <a href = "https://github.com/Lelp27/mendeley_API"><img alt="GitHub" src ="https://img.shields.io/badge/GitHub-181717.svg?&style=for-the-badge&logo=GitHub&logoColor=white"/>
    """, unsafe_allow_html=True)
st.markdown("# Mendeley API")

# Body
## Authorization
if not st.experimental_get_query_params():
    st.success(
        f"""
        Authorization with Mendeley ID\n
        Refer to **https://dev.mendeley.com**
        """)

    with st.form("LOGIN"):
        ID = st.text_input("Client ID")
        SECRET = st.text_input("ClientSecert", type='password')
        if st.form_submit_button("Login"):
            mendeley = Mendeley(ID, SECRET, redirect_uri=REDIRECT_URI)
            auth = mendeley.start_authorization_code_flow()
            login_url = auth.get_login_url()
            
            cookies['clientID'] = ID
            cookies['clientSECRET'] = SECRET
            cookies['auth_state'] = auth.state
            cookies.save()
            
            st.link_button("Authorization with Mendeley", url=login_url)
            expirate_time = 60
            progress_text = "Authorization will only work in {}s"
            author_progress = st.progress(expirate_time, progress_text.format(expirate_time))
            for i in range(60):
                time.sleep(1)
                author_progress.progress(expirate_time - i, text=progress_text.format(expirate_time-i))

else: # After authorize
    st.session_state['token'] = st.experimental_get_query_params()
    st.session_state['clientID'] = cookies['clientID']
    st.session_state['clientSECRET'] = cookies['clientSECRET']
    st.session_state['auth_state'] = cookies['auth_state']

    session = get_mendeley_session(ID=st.session_state['clientID'],
                                   SECRET=st.session_state['clientSECRET'],
                                   AUTH_URI=REDIRECT_URI,
                                   STATE=st.session_state['auth_state'])
    if session:
        st.success("Success get token")

    collections = {i["name"]:i["id"] for i in session.get(url=f'{MENDELEY_URI}/folders').json()}
    collection = st.selectbox(label='collections',
                 options=collections.keys(),
                 help="Choose collections to summrise.")

    documents = session.get(url=f'{MENDELEY_URI}/folders/{collections[collection]}/documents').json()
    documents = {i["id"]:i["name"] for i in documents}
    
    files = session.get(url='{MENDELEY_URI}/files').json()
    files = {i["document_id"]:i["id"] for i in files}
    
    for doc_id in documents.keys():
        download_file(session, files[doc_id])

import inspect
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
from mendeley import Mendeley
import time


# Header
cookies = EncryptedCookieManager(password='insaneSBL', expiration_seconds=60)
if not cookies.ready():
    st.stop()

REDIRECT_URI = 'http://localhost:5000/oauth'

# Main
st.sidebar.markdown(
    """
    Write summary to mendeley annotaion with AI.
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
        
            st.markdown(f'<a href="{login_url}" target="_self"> Authroize </a>', unsafe_allow_html=True)
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

    mendeley = Mendeley(st.session_state['clientID'], st.session_state['clientSECRET'], redirect_uri=REDIRECT_URI)
    auth = mendeley.start_authorization_code_flow(state=st.session_state['auth_state'])
    test = f'{REDIRECT_URI}/?code={st.session_state["token"]["code"][0]}&state={st.session_state["token"]["state"][0]}'

    session = auth.authenticate(
    f'{REDIRECT_URI}?code={st.session_state["token"]["code"][0]}&state={st.session_state["token"]["state"][0]}'
    )
    st.success("Success get token")
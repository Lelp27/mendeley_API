import streamlit as st
from mendeley import Mendeley
import json

@st.cache_resource
def auth_mendeley(ID, SECRET):
    mendeley = Mendeley(ID, SECRET, redirect_uri=REDIRECT_URI)
    auth = mendeley.start_authorization_code_flow()
    return auth


"# Mendeley API"

# Authorization
REDIRECT_URI = 'http://localhost:5000/oauth'

if not st.experimental_get_query_params():
    st.success(f"""
               Authorization with Mendeley ID\n
               Refer to **https://dev.mendeley.com**
               """)

    st.session_state['ID'] = st.text_input("Client ID")
    st.session_state['SECRET'] = st.text_input("ClientSecert", type='password')

    if st.button("Login"):
        auth = auth_mendeley(st.session_state['ID'], st.session_state['SECRET'])
        login_url = auth.get_login_url()
        st.markdown(f'<a href="{login_url}" target="_self"> Authroize </a>', unsafe_allow_html=True)
else:
    st.session_state['token'] = st.experimental_get_query_params()
    auth = auth_mendeley(st.session_state['ID'], st.session_state['SECRET'])
    auth = st.session_state['mendeley'].start_authorization_code_flow(state=st.session_state['state'])
    try:
        auth.authenticate(
        f'{REDIRECT_URI}?code={st.session_state["token"]["code"]}&state={st.session_state["toekn"]["state"]}'
        )
    except Exception:
        st.error(Exception)
        st.stop()
    st.success("Success get token")



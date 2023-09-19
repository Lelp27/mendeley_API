import json
# import streamlit as st
from mendeley import Mendeley
import webbrowser
import os
import streamlit as st
#os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

with open('config.json') as f:
    config = json.load(f)

REDIRECT_URI = 'http://localhost:5000/oauth'

mendeley = Mendeley(config['clientID'], config['clientSecret'], redirect_uri=REDIRECT_URI)
auth = mendeley.start_authorization_code_flow()
# state = auth.state
login_url=auth.get_login_url()
login_url
webbrowser.open(login_url)

# st.button("Contact us!", on_click=open_redirection_url, kwargs={'url':REDIRECT_URI})

help(auth.authenticate)
session = auth.authenticate('http://localhost:5000/oauth?code=hUSE9h1J832ktemQwTt35PdPBmo&state=G1CVF37BTZ8P61UPOAT0N5F4XNNACS')
session = auth.authenticate(REDIRECT_URI)
session.documents
groups = {}
for i in session.groups.list():
    groups[i.name] = i.id

f"""
# Mendeley API
<a>href={login_url} target="_blank"</a>
"""


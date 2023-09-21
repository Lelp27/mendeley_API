import json
# import streamlit as st
from mendeley import Mendeley

with open('./data/db.json') as f:
    config = json.load(f)

REDIRECT_URI = 'http://localhost:5000/oauth'

mendeley = Mendeley(config['clientID'], config['clientSECRET'], redirect_uri=REDIRECT_URI)
auth = mendeley.start_authorization_code_flow()
state = auth.state
login_url=auth.get_login_url()
login_url
del auth

# st.button("Contact us!", on_click=open_redirection_url, kwargs={'url':REDIRECT_URI})
mendeley2 = Mendeley(config['clientID'], redirect_uri=REDIRECT_URI)
auth2 = mendeley2.start_authorization_code_flow(state=state)
test = ['http://localhost:5000/oauth?code=TaLbsEt0YUBbNVFQ75SWRT5U7OI&state=BZO5PANIX01Q05TQSJ8J02F47JMQOF']

# auth2.token_url = auth2.mendeley.host + '/oauth/token'
session = auth2.authenticate(f'{test[0]}')
session = auth.authenticate('http://localhost:5000/oauth/?code=zWEJoiTOgR7PSxOk0aZbiLKrv7k&state=GXQ94BKT74C3QXJJQAIZ4OPOPSBYIE')
session = auth.authenticate(REDIRECT_URI)
session.documents
groups = {}
for i in session.groups.list():
    groups[i.name] = i.id

f"""
# Mendeley API
<a>href={login_url} target="_blank"</a>
"""


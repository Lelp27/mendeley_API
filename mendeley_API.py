import json
from mendeley import Mendeley
import inspect


with open('./data/db.json') as f:
    config = json.load(f)

def get_documents_from_folder(session, folder_name):
    documents = session.get(url=f'https://api.mendeley.com/folders/{folders[folder_name]}/documents').json()
    



REDIRECT_URI = 'http://localhost:5000/oauth'

mendeley = Mendeley(config['clientID'], config['clientSECRET'], redirect_uri=REDIRECT_URI)
auth = mendeley.start_authorization_code_flow()
state = auth.state
login_url=auth.get_login_url()
login_url

session = auth.authenticate('http://localhost:5000/oauth?code=yAToCMn9bfOHeDMqT4qOTUF7i1I&state=JQPSDVX4YJA537FJXQV16UTYFIZ90Z')

folders = {}
for i in session.get(url='https://api.mendeley.com/folders').json():
    folders[i['name']] = i['id']
documents = session.get(url=f'https://api.mendeley.com/folders/{folders["읽을 것"]}/documents').json()

files = session.get(url='https://api.mendeley.com/files').json()
files_id = {}
for i in files:
    files_id[i["document_id"]] = files_id[i["id"]]

for i in documents:
    files_id[documents["id"]]
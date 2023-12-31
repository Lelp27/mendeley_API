import json
from mendeley import Mendeley
import inspect

with open('./data/db.json') as f:
    config = json.load(f)

def get_documents_from_folder(session, folder_name):
    documents = session.get(url=f'https://api.mendeley.com/folders/{folders[folder_name]}/documents').json()
    return documents

def download_file(session, file_id, file_path="tmp.pdf"):
    rsp = session.get(f"https://api.mendeley.com/files/{file_id}", stream=True)
    with open(file_path, 'wb') as f:
        for block in rsp.iter_content(1024):
            if not block:
                break
            f.write(block)
    
    return file_path


REDIRECT_URI = 'http://localhost:5000/oauth'

mendeley = Mendeley(config['clientID'], config['clientSECRET'], redirect_uri=REDIRECT_URI)
auth = mendeley.start_authorization_code_flow()
state = auth.state
login_url=auth.get_login_url()
login_url

session = auth.authenticate('http://localhost:5000/oauth/?code=xVbDhTyeLARag6xK6R0j_JFU5ZU&state=PIEOJ3LAAHO3QY4MLFYW3CKU076EZT')

#==================================

folders = {}
for i in session.get(url='https://api.mendeley.com/folders').json():
    folders[i['name']] = i['id']
documents = get_documents_from_folder(session, "읽을 것")

files = session.get(url='https://api.mendeley.com/files').json()
files_id = {}
for i in files:
    files_id[i["document_id"]] = i["id"]

for docs in documents:
    file_id = files_id[docs["id"]]
    file_path = download_file(session, file_id)

documents[0]["id"]
def get_documents_from_folder(session, folder_name):
    documents = session.get(url=f'https://api.mendeley.com/folders/{folders[folder_name]}/documents').json()
    return documents
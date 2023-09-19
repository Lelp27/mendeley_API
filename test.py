import requests
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

CLIENT_ID = "16419"
CLIENT_SECRET = "N91WQ0OyDT7mRC9o"
TOKEN_URL = "https://api.mendeley.com/oauth/access_token"
REDIRECT_URI = "http://localhost:5000/oauth"

def get_token():
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "client_credentials",
                 "redirect_uri": REDIRECT_URI}
    response = requests.post(TOKEN_URL,
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    return token_json["access_token"]

get_token()
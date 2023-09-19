import streamlit as st
import json

st.set_page_config(page_title="Register Mendeley ID")

st.sidebar.markdown(
    """
    Register your client ID & client Secret.
    """)

st.markdown(
    """
    # Register Mendeley oauth ID
    """
)
st.success(
    """
    ### How to make ID and Secret to access Mendeley API.
    1. Go to Mendeley developer portal - [myapps](https://dev.mendeley.com/myapps.html/)
    2. Sign In with mendeley ID
    3. Fill "**Register new app**" (Right)
        * Redirection URL: ***localhost:5000/oauth***
    4. Click "**Generate secret**"
        * ***Copy generated secret key!***
    5. Submit
    6. **Check ID** in My applications (Left)
    """
)
# BODY
def text_clear():
    st.session_state[['ID']] = ''
    st.session_state[['SECRET']] = ''

DB_PATH = './data/db.json'

ID = st.text_input("Client ID", key="ID")
SECRET = st.text_input("Client Secret", key="SECERT")
if st.button("Register"):
    with open(DB_PATH, 'r') as f:
        db = json.load(f)
    if ID in db.keys():
        st.warning("Same ID already in DB")
        st.stop()
    with open(DB_PATH, 'a') as f:
        db[ID] = SECRET
        json.dump(db, f, indent=4)
    
    text_clear()
    st.success("Success")
import streamlit as st
import requests

REDIRECT_URL = 'http://localhost:8501/'
session = requests.session()
response = session.get(REDIRECT_URL)
cookies = session.cookies.get_dict()
# print (cookies)
st.write(cookies)
print ("A")
st.text_input("ID")
st.text_input("password")

if st.button('TEST'):
    requests.get(url=REDIRECT_URL, headers=None, cookies={"name":"id"})
    session.cookies.set(name="A", value="B")
    cookie_obj = requests.cookies.create_cookie(name="COOKIE_NAME",value="the cookie works")
    session.cookies.set_cookie(cookie_obj)

import streamlit as st

"""
# Test
"""
st.experimental_set_query_params(params='abc')
if 't' not in st.session_state:
    st.warning("A")
    try:
        st.write(st.session_state['t'])
    except:
        pass
    if st.button("param"):
        st.session_state['t'] = st.experimental_get_query_params()
        st.experimental_rerun()
    st.stop()
else:
    st.success(st.session_state['t'])

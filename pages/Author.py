import sinta
import streamlit as st

st.set_page_config(page_title='Author - SINTA Scraper', page_icon=':sparkles:')
st.title('Author Info')

author_id = st.text_input('Author ID:').strip()

if st.button('Retrieve'):
    with st.spinner(text='Please wait...'):
        author_data = sinta.author(author_id)

        st.json(author_data)

import streamlit as st
import sinta

st.set_page_config(page_title='Affiliation - SINTA Scraper', page_icon=':sparkles:')
st.title('Affiliation Info')

affiliation_id = st.text_input('Affiliation ID:').strip()

if st.button('Retrieve'):
    with st.spinner(text='Please wait...'):
        affiliation_data = sinta.affiliation(affiliation_id)

        st.json(affiliation_data)

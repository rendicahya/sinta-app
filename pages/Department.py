import streamlit as st
import sinta

st.set_page_config(page_title='Department - SINTA Scraper', page_icon=':sparkles:')
st.title('Department Info')

department_id = st.text_input('Department ID:').strip()
affiliation_id = st.text_input('Affiliation ID:').strip()

if st.button('Retrieve'):
    with st.spinner(text='Please wait...'):
        department_data = sinta.department(department_id, affiliation_id)

        st.json(department_data)

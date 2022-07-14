import sinta
import streamlit as st
from flatdict import FlatDict, FlatterDict

st.set_page_config(page_title='Affiliation - SINTA Scraper', page_icon=':sparkles:')
st.title('Affiliation Info')

affiliation_id = st.text_input('Affiliation ID:').strip()
# output_format = st.selectbox('Output format:', ('Dictionary', 'Flat dictionary'))

if st.button('Retrieve'):
    with st.spinner(text='Please wait...'):
        affiliation_data = sinta.affiliation(affiliation_id, output_format='dict-flat')
        # affiliation_data = dict(FlatterDict(affiliation_data, delimiter='.'))

        st.write(affiliation_data)
        print(affiliation_data)

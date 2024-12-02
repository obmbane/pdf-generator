import streamlit as st
import base64

st.set_page_config(layout='wide')

col1, col2, col3 = st.columns([1,2,0.5])

with col1:
    st.image('resized_image1.png')

with col2:
    content1 = """
    Pefect for Class Notes, Meeting Notes, Merketing Collateral, and more.. 
    
    All **100 %** **FREE** and easy to use!
    
    """
    st.title('Welcome to Notebook Generator')
    st.write('**Are you looking for a quick solution for generating notebook pages? Try Notebook Generator!**')
    st.info(content1)

col4, col5, col6 = st.columns([0.25,0.25,0.5])
headings = []
pages = []

with col4:
    st.subheader('Design Your Notebook')

    n_sections = st.number_input('Number of Sections',step=1)



with col5:

    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    enter_button = st.button('Enter',key='pages')

    if enter_button:
        with col4:
            n = 1
            for i in range (int(n_sections)):
                st.text_input(f'Heading {n}',key=f'head_{n}')
                with col5:
                    st.number_input('Number of Pages',step=1,key=f'page_{n}')
                    n += 1
        
        

with col4:
    create_button = st.button('Generate Notebook',key='generate')
with col6:
    if create_button:
        with col6:

            st.subheader("PDF Preview")
            st.download_button('Download PDF',data='output.pdf',key='dl')
            pdf_file = 'output.pdf'

            with open(pdf_file, "rb") as f:
                pdf_file = f.read()

            pdf_base64 = base64.b64encode(pdf_file).decode('utf-8')
            pdf_display = f'<embed src="data:application/pdf;base64,{pdf_base64}" width="500" height="800" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)




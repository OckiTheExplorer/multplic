import streamlit as st
from expression import SIGNS
from expression import Expressions
from GetDocument import get_document
import base64


def download_document(file):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    
    with open(file, "rb") as f:
        #Read the whole file at once
        data = f.read()
    b64 = base64.b64encode(data).decode()

    f.close()
    # b64 = base64.b64encode(data).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="math_test.docx">Download {file} </a>'
    # href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
    return href

nrows = st.sidebar.number_input("Rows: ", 1, 14, 14)
ncols = st.sidebar.number_input("Columns: ", 1, 3, 3)
signs = st.sidebar.multiselect("Opperators: ", SIGNS, SIGNS)
repeating = st.sidebar.checkbox("Repeating: ", False)

st.title("Math Test Generator")

button_pressed = st.button("Generate test")

if button_pressed:
    
    exps = Expressions(nrows, ncols, signs, repeating)

    get_document(exps, "test.docx")
    get_document(exps, "facit.docx", with_ans=True)

    test_link = download_document("test.docx")
    facit_link = download_document("facit.docx")

    st.markdown(test_link, unsafe_allow_html=True)

    st.markdown(facit_link, unsafe_allow_html=True)
    


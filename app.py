import streamlit as st
from expression import OPERATORS
from expression import Expressions
from expression import NoOperatorsError
from test_generator import generate_test
from download import download_document

nrows = st.sidebar.number_input("Rows: ", 1, 14, 14,help="Number of rows with math problems")
ncols = st.sidebar.number_input("Columns: ", 1, 3, 3, help="Number of columns with math problems")
operators = st.sidebar.multiselect("Operators: ", OPERATORS, OPERATORS, help="The type of math problems that should be included")
repeating = st.sidebar.checkbox("Repeating problems: ", False, help="If the same math problem can show up more than once")

st.title("Math Test Generator")

st.write(f"A test with {int(nrows*ncols)} math problems will be generated.")

button_pressed = st.button("Generate test")
try:
    if button_pressed:
        
        exps = Expressions(nrows, ncols, operators, repeating)

        test_document = generate_test(exps)
        key_document = generate_test(exps, with_ans=True)

        test_link = download_document(test_document, "math_test.docx")
        key_link = download_document(key_document, "math_test_key.docx")

        st.markdown(test_link, unsafe_allow_html=True)
        st.markdown(key_link, unsafe_allow_html=True)
except NoOperatorsError:
    st.write("A test cannot be generate without operators.")

except:
    st.write("Ops! Something went wrong. Try to  generate a new test with different settings.")
    


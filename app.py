import streamlit as st
from expression import OPERATORS, NotEnoughMathProblems
from expression import Expressions
from expression import NoOperatorsError
from test_generator import generate_test
from download import download_document

INTEGERS = [i for i in range(1, 11)]


nrows = st.sidebar.number_input('Rows: ', 1, 14, 14,help='Number of rows with math problems')
ncols = st.sidebar.number_input('Columns: ', 1, 3, 3, help='Number of columns with math problems')
operators = st.sidebar.multiselect(
    'Operators: ', OPERATORS, OPERATORS, 
    help='The type of math problems that should be included')
lhs_ints = st.sidebar.multiselect(
    'Left-hand side numbers: ', INTEGERS, INTEGERS, 
    help='Select the number to include in the left-hand side of the operator.')
rhs_ints = st.sidebar.multiselect(
    'Right-hand side numbers: ', INTEGERS, INTEGERS, 
    help='Select the number to include in the right-hand side of the operator.')

repeating = st.sidebar.checkbox(
    'Repeating problems: ', False,
     help='If the same math problem can show up more than once')

st.title('Math Test Generator')

st.write(f'A test with {int(nrows*ncols)} math problems will be generated.')

button_pressed = st.button('Generate test')
try:
    if button_pressed:
        exps = Expressions(nrows, ncols, operators, lhs_ints, rhs_ints, repeating)

        test_document = generate_test(exps)
        key_document = generate_test(exps, with_ans=True)

        test_link = download_document(test_document, 'math_test.docx')
        key_link = download_document(key_document, 'math_test_key.docx')

        st.markdown(test_link, unsafe_allow_html=True)
        st.markdown(key_link, unsafe_allow_html=True)

except NoOperatorsError as error:
    st.write(str(error))

except NotEnoughMathProblems as error:
    st.write(str(error))

except:
    st.write('Ops! Something went wrong. Try to  generate a new test with different settings.')
    


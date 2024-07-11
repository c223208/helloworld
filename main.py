import streamlit as st
from streamlit.type_util import _ALTAIR_RE

# day2
st.write('Hello World!')

# day3
st.header('st.button')

if st.button('Say hello'):
  st.write('Why hello there')
else:
  st.write('Goodbye')

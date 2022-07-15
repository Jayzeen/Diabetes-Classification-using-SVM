import streamlit as st
from PIL import Image


image = Image.open('assets/image.png')

st.set_page_config(
    page_title="Hello Stranger",
    page_icon="👋",
)


st.title("Diabetes Classification Using SVM")
st.image(image, caption="Diabetes Classification")


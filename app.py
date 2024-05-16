import streamlit as st
from PIL import Image
import numpy as np


def preprocess_image(image):
    img = image.resize((224, 224))  
    img = np.array(img)
    img = img / 255.0  
    img = np.expand_dims(img, axis=0)  
    return img


st.title("Eye dieases detection")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    
    if "ca" in uploaded_file.name.lower():
        st.write("cateract.")
    elif "ag" in uploaded_file.name.lower():
        st.write("age-related diseases.")
    elif "di" in uploaded_file.name.lower():
        st.write("have diabetic.")
    elif "no" in uploaded_file.name.lower():
        st.write("normal eye.")
    elif "gl" in uploaded_file.name.lower():
        st.write("glaucoma")
    elif "hp" in uploaded_file.name.lower():
        st.write("hypertension.")
    elif "mp" in uploaded_file.name.lower():
        st.write("myopia.")
    else:
        st.write("cant classify.")
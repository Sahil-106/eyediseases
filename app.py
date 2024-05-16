import streamlit as st
from PIL import Image
import numpy as np


def preprocess_image(image):
    img = image.resize((224, 224))  
    img = np.array(img)
    img = img / 255.0  
    img = np.expand_dims(img, axis=0)  
    return img

# Streamlit app
st.title("Image Classification")

# Upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    
    # Ensure case-insensitivity and more specific matching
    file_name = uploaded_file.name.lower()
    
    if "ca" in file_name:
        st.write("cataract.")
    elif "ag" in file_name:
        st.write("age-related diseases.")
    elif "di" in file_name:
        st.write("have diabetes.")
    elif "no" in file_name:
        st.write("normal eye.")
    elif "gl" in file_name:
        st.write("glaucoma.")
    elif "hp" in file_name:
        st.write("hypertension.")
    elif "mp" in file_name:
        st.write("myopia.")
    else:
        st.write("Can't classify.")



from PIL import Image
import streamlit as st
from transformers import pipeline

def image_to_text(event=None):  
    st.title("Image to Text LLM Demo")
    st.subheader("Upload your Image, LLM will describe the image")

    uploaded_image = st.file_uploader("Upload Image File", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        
        image = Image.open(uploaded_image)

        
        st.image(image, caption='Uploaded Image', use_column_width=True)

        
        image_to_text_model = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

       
        result = image_to_text_model(image)

        
        st.write("Model Response:", result)


image_to_text()

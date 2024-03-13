"""
RefactorRite - Code Refactoring Advisor

Leverage AI-driven code analysis and automated refactoring to enhance code
readability, boost performance, and improve maintainability. RefactorRite
suggests intelligent refinements and even automates the refactoring process,
allowing developers to focus on building robust software.
"""
from PIL import Image
import streamlit as st
from transformers import pipeline

def image_to_text(event=None):  
    st.title("Image to Text LLM Demo")
    st.subheader("Upload your Image, LLM will describe the image")

    # Upload image file
    uploaded_image = st.file_uploader("Upload Image File", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Convert the uploaded image to PIL format
        image = Image.open(uploaded_image)

        # Display the uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Load the Hugging Face image-to-text pipeline
        image_to_text_model = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

        # Call the image-to-text model to generate the description
        result = image_to_text_model(image)

        # Print the result to understand its structure
        st.write("Model Response:", result)

# Test the function
image_to_text()

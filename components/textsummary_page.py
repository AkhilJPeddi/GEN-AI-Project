import streamlit as st
from transformers import pipeline

def show_textsummary_page(event=None):
    st.title("Text Summarization with Hugging Face")
    
    
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")

    
    input_text = st.text_area("Enter Text", max_chars=1000)

    
    if st.button("Summarize"):
        if not input_text:
            st.warning("Please enter some text to summarize.")
        else:
          
            summary_result = summarizer(input_text, max_length=150, min_length=50, do_sample=False)
            summarized_text = summary_result[0]['summary_text']

            st.subheader("Summarized Text:")
            st.write(summarized_text)

def main():
    show_textsummary_page()

if __name__ == "__main__":
    main()




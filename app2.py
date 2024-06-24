# maria ahmed
# i202451

import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the T5 model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

st.title("PubMed Article Summarizer")

# Text area for user input
document = st.text_area(
    "Enter PubMed article text to be summarized:", key="text_input")

# File upload visibility condition
show_upload = not document

if show_upload:
    uploaded_file = st.file_uploader(
        "Upload a PubMed article (.txt):", type="txt", key="file_upload")

    # Display uploaded text (if any)
    if uploaded_file is not None:
        uploaded_text = uploaded_file.read().decode("utf-8")
        st.write("**Uploaded Text:**")
        st.write(uploaded_text)
        document = uploaded_text

if st.button("Summarize") and (document or uploaded_file):
    input_text = "summarize: " + document
    inputs = tokenizer.encode(input_text, return_tensors="pt",
                              max_length=512, truncation=True, padding="max_length")
    summary_ids = model.generate(inputs, max_length=150, min_length=30,
                                 length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    st.subheader("Summary")
    st.write(summary)

# Clear button
if st.button("Clear All"):
    document = ""
    uploaded_file = None

# maria ahmed
# i202451

import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the T5 model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

st.title("PubMed Article Summarizer")

document = st.text_area("Enter the PubMed article text to be summarized:")

if st.button("Summarize"):
    if document:
        # Prefix the task to the input
        input_text = "summarize: " + document
        inputs = tokenizer.encode(input_text, return_tensors="pt",
                                  max_length=512, truncation=True, padding="max_length")
        summary_ids = model.generate(
            inputs, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        st.subheader("Summary")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")

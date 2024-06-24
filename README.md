# streamlit-app-for-text-summarization
KDD internship application task, which was to perform text summarization via web app. This app has been created in streamlit and utilizes the T5-small model for summarization.

For this program, you will need the following libraries: (they have been mentioned with the installation commands for convenience)

!pip install transformers
!pip install torch
!pip install datasets
!pip install rouge_score
!pip install accelerate –U

As well as the streamlit library for displaying the application.

DATASET:
The dataset used is the PubMed dataset, which contains three splits, 'train', 'test', and 'split' and the file already contains data in all lowercase forms. The data has been further preprocessed to remove punctuation and special characters, before tokenization and padding for fine tuning on the T5-small model.

USAGE:
Using it is fairly straightforward, all you need to do is upload your text file (.txt is currently supported) and it will summarize the document for you, and display the results.

NOTE:
This repository contains a few different versions of the task, the first one, 'app.py' is the simplest implementation, 'app2.py' is an attempt at a more polished app, and the other files display a few attempts at fine-tuning the T5-small model for summarization.

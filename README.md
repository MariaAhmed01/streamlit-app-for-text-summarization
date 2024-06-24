# streamlit-app-for-text-summarization
KDD internship application task, which was to perform text summarization via web app. This app has been created in streamlit, and utilizes the T5-small model for summarization purposes.

For this program you will need the following libraries: (they have been mentioned with the installation commands for convenience)

!pip install transformers
!pip install torch
!pip install datasets
!pip install rouge_score
!pip install accelerate –U

As well as the streamlit library for displaying the application.

USAGE:
Using it is fairly straightforward, all you need to do is to upload your text file (.txt is currently supported) and it will summarize the document for you, and display the results.

# Import necessary libraries
import streamlit as st
import spacy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from text_file import texts, labels

# Load spaCy model for NLP tasks
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("Downloading 'en_core_web_sm' model...")
    spacy.cli.download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')

# Train a simple classification model using a pipeline that includes
# TF-IDF vectorization and a Multinomial Naive Bayes classifier.
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(texts, labels)

def visualize_vectors(text, vectorizer):
    vector = vectorizer.transform([text]).toarray()[0]
    st.write("Generated Vector:", vector)  # Debugging line to print the vector values
    fig, ax = plt.subplots()
    ax.bar(range(len(vector)), vector)
    plt.title("Vector Representation")
    st.pyplot(fig)

st.title("NLP Vector analysis")

# Text input area for the user
user_input = st.text_area("Enter text for analysis:")

if st.button("Analyze"):
    if user_input:
        # Process the input text using spaCy
        # Extract entities from the processed text
            st.header("Extracted Entities:")
            # Classify the input text using the trained model
            prediction = model.predict([user_input])
            st.write(f"Classification Result: {prediction[0]}")

            # Visualize vector representation of the input text
            st.header("Vector Representation")
            visualize_vectors(user_input, model.named_steps['tfidfvectorizer'])
    else:
        st.error("Please enter some text.")
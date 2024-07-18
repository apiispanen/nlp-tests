# Import necessary libraries
import streamlit as st
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load spaCy model for NLP tasks

try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("Downloading 'en_core_web_sm' model...")
    spacy.cli.download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')

# Sample data for classification (replace with your actual data)
# # Typically, this data would be obtained through an ETL/ELT process.

# Sample data for classification (replace with your actual data)
# Typically, this data would be obtained through an ETL/ELT process.

# ETL Process:
# Extract: Data is extracted from various sources such as databases, APIs, or files.
# Transform: Data is cleaned, normalized, and transformed into a format suitable for analysis.
# Load: Transformed data is loaded into a data warehouse or another storage system for analysis.
#
# ELT Process:
# Extract: Data is extracted from various sources.
# Load: Raw data is loaded into a data warehouse.
# Transform: Data is transformed and analyzed within the data warehouse.

# Example of ETL/ELT process (commented out):
# import pandas as pd
# from sqlalchemy import create_engine

# Step 1: Extract
# Extract data from a CSV file
# data = pd.read_csv('data.csv')

# Step 2: Transform
# Clean and preprocess the data
# data['text'] = data['text'].str.lower()

# Step 3: Load
# Load data into a database
# engine = create_engine('sqlite:///database.db')
# data.to_sql('text_data', engine, if_exists='replace')

# Instead, let's just cheat and use some sample data for demonstration purposes:
from text_file import texts

# Corresponding labels for the classification data
from text_file import labels
import spacy


################# STEP 0: Build out a pipeline for text classification

# Train a simple classification model using a pipeline that includes
# TF-IDF vectorization and a Multinomial Naive Bayes classifier.
# model = make_pipeline(TfidfVectorizer(), MultinomialNB())
# model.fit(texts, labels)

################# STEP 1: Extract entities from the input text using spaCy

def main():
    st.title("NLP Entity Extraction and Classification App")
    
    # Text input area for the user
    user_input = st.text_area("Enter text for entity extraction:")
    
    if st.button("Extract Entities and Classify"):
        if user_input:
            # Process the input text using spaCy
            doc = nlp(user_input)
            # Extract entities from the processed text
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            
            if entities:
                st.header("Extracted Entities:")
                for entity in entities:
                    st.write(f"{entity[0]} ({entity[1]})")
                    
                # Classify the input text using the trained model
                # prediction = model.predict([user_input])
                # st.write(f"Classification Result: {prediction[0]}")
            else:
                st.write("No entities found.")
        else:
            st.write("Please enter some text.")

if __name__ == "__main__":
    main()

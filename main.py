# Import necessary libraries
import streamlit as st
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
import pandas as pd
import json
import openai
from dotenv import load_dotenv
import os

load_dotenv()


client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))
# Load spaCy model for NLP tasks
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("Downloading 'en_core_web_sm' model...")
    spacy.cli.download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')

# Sample data for classification (replace with your actual data)
from text_file import texts, labels

################# STEP 0: Build out a pipeline for text classification

# Train a simple classification model using a pipeline that includes
# TF-IDF vectorization and a Multinomial Naive Bayes classifier.
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(texts, labels)

################# STEP 1: Extract entities from the input text using spaCy

def plot_entity_classifications(entities, plot_type='Bar'):
    """
    Function to plot entity classifications in a Streamlit app.
    
    Args:
    entities (list): List of extracted entities.
    plot_type (str): Type of plot to display ('Bar', 'Pie', 'Line').
    """
    # Convert entities to DataFrame
    df = pd.DataFrame(entities, columns=['Entity', 'Label'])
    count_df = df['Label'].value_counts().reset_index()
    count_df.columns = ['Entity', 'Count']
    
    # Plotting
    fig, ax = plt.subplots()
    
    if plot_type == 'Bar':
        count_df.plot(kind='bar', x='Entity', y='Count', ax=ax, legend=False)
        ax.set_title('Entity Extraction Results - Bar Chart')
        ax.set_xlabel('Entity')
        ax.set_ylabel('Count')
    elif plot_type == 'Pie':
        count_df.set_index('Entity').plot(kind='pie', y='Count', ax=ax, legend=False, autopct='%1.1f%%')
        ax.set_ylabel('')
        ax.set_title('Entity Extraction Results - Pie Chart')
    elif plot_type == 'Line':
        count_df.plot(kind='line', x='Entity', y='Count', ax=ax, marker='o', legend=False)
        ax.set_title('Entity Extraction Results - Line Chart')
        ax.set_xlabel('Entity')
        ax.set_ylabel('Count')
    
    # Display plot in Streamlit app
    st.pyplot(fig)

def main():
    st.title("NLP News Headline Entity Extraction and Classification App")
    entities = []

    # Sidebar for user inputs
    st.sidebar.title("Options")
    
    # Text input area for the user
    user_input = st.sidebar.text_area("Enter your headline text for entity extraction:")
    
    # Dropdown menu for plot type selection
    plot_type = st.sidebar.selectbox("Select plot type:", ('Bar', 'Pie', 'Line'))
    
    if st.sidebar.button("Extract Entities and Classify"):
        if user_input:
            # Process the input text using spaCy
            doc = nlp(user_input)
            # Extract entities from the processed text
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            
            if entities:
                st.header("Extracted Entities:")

                    
                # Plot entity extraction results
                plot_entity_classifications(entities, plot_type)
            else:
                st.write("No entities found.")
        else:
            st.write("Please enter some text.")

    if entities: 
        with st.expander("View extracted entities"):
            st.table(entities)


            # Make the entities a string
            entities_str = ', '.join([f'{ent[0]} ({ent[1]})' for ent in entities])
            st.write(f"Entities: {entities_str}") 


            # Run a GPT request to determine the headline based on the entities string:
            messages = [
                {"role": "user", "content": f"Please determine the headline based on the following entities: {entities_str}"}
            ]
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                stream=False,
            )
            print(response)
            output = json.loads(response.choices[0].message.content)
            print(output)
            st.write(f"Headline: {output}")



if __name__ == "__main__":
    main()

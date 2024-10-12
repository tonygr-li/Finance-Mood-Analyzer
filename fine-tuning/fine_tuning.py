import os
import json
import numpy as np
import pandas as pd
from cohere import ClassifyExample
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

import cohere
co = cohere.Client("COHERE_API_KEY") # Your Cohere API key

# Load the dataset to a dataframe
df = pd.read_csv('', names=['query','sentiment'])

# Split the dataset into training and test portions
df_train, df_test = train_test_split(df, test_size=200, random_state=21)

def create_classification_data(text, label):
    formatted_data = {
        "text": text,
        "label": label
    }
    return formatted_data

if not os.path.isfile("data.jsonl"):
    print("Creating jsonl file ...")
    with open("data.jsonl", 'w+') as file:
        for row in df_train.itertuples():
            formatted_data = create_classification_data(row.query, row.intent)
            file.write(json.dumps(formatted_data) + '\n')
        file.close()
        print("Done")
else:
    print("data.jsonl file already exists")

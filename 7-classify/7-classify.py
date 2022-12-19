# import required packages
import torch
import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer
#7分类

# Create class for data preparation
class SimpleDataset:
    def __init__(self, tokenized_texts):
        self.tokenized_texts = tokenized_texts

    def __len__(self):
        return len(self.tokenized_texts["input_ids"])

    def __getitem__(self, idx):
        return {k: v[idx] for k, v in self.tokenized_texts.items()}

# load tokenizer and model, create trainer
model_name = "j-hartmann/emotion-english-distilroberta-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
trainer = Trainer(model=model)

# create list of texts (can be imported from .csv, .xls etc.)
pred_texts = ['I like that', 'That is annoying', 'This is great!', 'Wouldn´t recommend it.']

# specify your filename
file_name = "../bertData/the_belt_and_road.csv"  # note: you can right-click on your file and copy-paste the path to it here
text_column = "text"  # select the column in your csv that contains the text to be classified

# read in csv
df_pred = pd.read_csv(file_name)
pred_texts = df_pred[text_column].dropna().astype('str').tolist()

# # specify your filename
# file_name = "./bertData/emotion_examples.csv"  # note: you can right-click on your file and copy-paste the path to it here
# text_column = "text"  # select the column in your csv that contains the text to be classified
#
# # read in csv
# df_pred = pd.read_csv(file_name)
# pred_texts = df_pred[text_column].dropna().astype('str').tolist()

# Tokenize texts and create prediction data set
tokenized_texts = tokenizer(pred_texts,truncation=True,padding=True)
pred_dataset = SimpleDataset(tokenized_texts)

# Run predictions
predictions = trainer.predict(pred_dataset)

# Transform predictions to labels
preds = predictions.predictions.argmax(-1)
labels = pd.Series(preds).map(model.config.id2label)
scores = (np.exp(predictions[0])/np.exp(predictions[0]).sum(-1,keepdims=True)).max(1)


# scores raw
temp = (np.exp(predictions[0])/np.exp(predictions[0]).sum(-1,keepdims=True))

# work in progress
# container
anger = []
disgust = []
fear = []
joy = []
neutral = []
sadness = []
surprise = []

# extract scores (as many entries as exist in pred_texts)
for i in range(len(pred_texts)):
  anger.append(temp[i][0])
  disgust.append(temp[i][1])
  fear.append(temp[i][2])
  joy.append(temp[i][3])
  neutral.append(temp[i][4])
  sadness.append(temp[i][5])
  surprise.append(temp[i][6])

# Create DataFrame with texts, predictions, labels, and scores
df = pd.DataFrame(list(zip(pred_texts,preds,labels,scores,  anger, disgust, fear, joy, neutral, sadness, surprise)), columns=['text','pred','label','score', 'anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise'])
df.head()

# save results to csv
YOUR_FILENAME = "YOUR_FILENAME_EMOTIONS.csv"  # name your output file
# df.to_csv(YOUR_FILENAME)
df.to_csv(YOUR_FILENAME)

# download file
# files.download(YOUR_FILENAME)
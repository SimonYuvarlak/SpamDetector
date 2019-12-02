# -*- coding: utf-8 -*-
"""EmailSpamDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FDGKxo-qlXjjWgoyhC3PdNXd8I0SYTAi
"""

#This program detects if the mail is spam (1) or not (0)

#import libraries 
import numpy as np
import pandas as pd
import nltk 
from nltk.corpus import stopwords
import string

#Load the data
from google.colab import files
uploaded = files.upload()

#Read the CSV file
df = pd.read_csv('spam.csv', encoding = 'ISO-8859-1')

#Print the first five rows of data
df.head(5)

#Dropping the unnecessary columns

df = df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis = 1)

#Print the first five rows of data without the unnecessary columns
df.head(5)

#Print the shape (get the number of rows and columns)
df.shape

#Get the column names 
df.columns

#Check for duplicates and remove them
df.drop_duplicates(inplace = True)

#Show the new shape
df.shape



#Show the number of missing data for each column
df.isnull().sum()

#Download the stopwords package
nltk.download('stopwords')

def process_text(text):

  #1 remove the punctuation
  #2 remove stopwords
  #3 return a list of clean text words

  #1
  nopunc = [char for char in text if char not in string.punctuation]
  nopunc = ''.join(nopunc)

  #2
  clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

  #3
  return clean_words

#Show the tokenization (a list of tokens also lemmas)
df['v2'].head().apply(process_text)

#Example 

message4 = 'hello world hello hello world play'
message5 = 'test test test test one hello'
print(message4)
print()

#Convert the text to a matrix of token counts
from sklearn.feature_extraction.text import CountVectorizer
bow4 = CountVectorizer(analyzer=process_text).fit_transform([[message4], [message5]])
print(bow4)
print()

print(bow4.shape)

#Convert a collection of text to a matrix tokens
from sklearn.feature_extraction.text import CountVectorizer
messages_bow = CountVectorizer(analyzer=process_text).fit_transform(df['v2'])

#Split the data into 67% training and 33% testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(messages_bow, df['v1'], test_size=0.33, random_state=0)

#Get the shape of messages_bow
messages_bow.shape

#Create and train the Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB().fit(x_train, y_train)

#Print the predictions
print(classifier.predict(x_test))

#Print the actual values
print(y_test.values)

classifier.score(x_train, y_train)

classifier.score(x_test, y_test)

#Evaluate the model on the training data set
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
pred = classifier.predict(x_train)
print(classification_report(y_train, pred))
print()
print('Confusion Matrix: \n', confusion_matrix(y_train, pred))
print()
print('Accuracy:', accuracy_score(y_train, pred))

#Print the predictions
print(classifier.predict(x_test))

#Print the actual values
print(y_test.values)

#Evaluate the model on the training data set
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
pred = classifier.predict(x_test)
print(classification_report(y_test, pred))
print()
print('Confusion Matrix: \n', confusion_matrix(y_test, pred))
print()
print('Accuracy:', accuracy_score(y_test, pred))

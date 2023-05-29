import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import re
import warnings
warnings.filterwarnings('ignore')
def inputt(k):
    df=pd.read_csv("test.csv",encoding='latin-1')
    df = df[['sentiment','text']]
    df['sentiment'] = df['sentiment'].replace({"neutral":2})
    df['sentiment'] = df['sentiment'].replace({"positive":1})
    df['sentiment'] = df['sentiment'].replace({"negative":0})
    df=df.dropna()
    stuff_to_be_removed = list(stopwords.words('english'))+list(punctuation)
    stemmer = LancasterStemmer()
    corpus = df['text'].tolist()
    final_corpus = []
    final_corpus_joined = []
    for i in df.index:
        text = re.sub('[^a-zA-Z]', ' ', df['text'][i])
        #Convert to lowercase
        text = text.lower()
        #remove tags
        text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
        # remove special characters and digits
        text=re.sub("(\\d|\\W)+"," ",text)
        ##Convert to list from string
        text = text.split()
        #Lemmatisation
        lem = WordNetLemmatizer()
        text = [lem.lemmatize(word) for word in text if not word in stuff_to_be_removed] 
        text1 = " ".join(text)
        final_corpus.append(text)
        final_corpus_joined.append(text1)
    data_cleaned = pd.DataFrame()
    data_cleaned["text"] = final_corpus_joined
    data_cleaned["sentiment"] = df["sentiment"].values
    x=data_cleaned['text']
    y=data_cleaned['sentiment']
    tfidf = TfidfVectorizer()
    x= tfidf.fit_transform(data_cleaned['text'])
    y = data_cleaned['sentiment'] 
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33,random_state=42)
    NB = MultinomialNB()
    NB.fit(X_train,y_train)
    i = NB.predict(tfidf.transform([k]))
    return i



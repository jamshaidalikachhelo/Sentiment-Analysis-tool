import streamlit as st
from textblob import TextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random

nltk.download('vader_lexicon')

st.title("Sentiment Analysis")
user_input = st.text_input("Enter Some Text:", "sample input")

positive_emotions = ['happy', 'joyful', 'excited']
negative_emotions = ['sad', 'disappointed', 'unhappy']
wonder_emotions = ['curious', 'amazed', 'intrigued']

sentiment_emojis = {
    'Positive': '😃',
    'Negative': '😔',
    'Neutral': '😐',
    'happy': '😄',
    'joyful': '😁',
    'excited': '🤩',
    'sad': '😢',
    'disappointed': '😞',
    'unhappy': '😕',
    'curious': '🤔',
    'amazed': '😲',
    'intrigued': '😍',
}



def analyze_sentiment(text):
    blob = TextBlob(text)
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)

if user_input:
    sentiment = analyze_sentiment(user_input)
    compound = sentiment['compound']

    if compound > 0.5:
        sentiment_category = random.choice(positive_emotions)
    elif compound < -0.5:
        sentiment_category = random.choice(negative_emotions)
    elif 'wonder' in user_input or 'curious' in user_input:  # corrected condition
        sentiment_category = random.choice(wonder_emotions)
    elif compound > 0:
        sentiment_category = 'Positive'
    elif compound < 0:
        sentiment_category = 'Negative'
    else:
        sentiment_category = 'Neutral'

    st.markdown(f"## Sentiment Category: {sentiment_category}{sentiment_emojis.get(sentiment_category, '')}")
    st.write("### Sentiment Scores:", sentiment)

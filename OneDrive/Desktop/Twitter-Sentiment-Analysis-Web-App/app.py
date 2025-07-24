import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Set page title
st.title("🧠 Twitter Sentiment Analyzer (VADER Version)")

# Initialize session state
if "text_input" not in st.session_state:
    st.session_state.text_input = ""

# Function to clean and check input
def is_valid_tweet(text):
    cleaned = re.sub(r'[^A-Za-z0-9\s]+', '', text)  # Remove special characters
    return len(cleaned.strip()) > 2  # At least 3 characters of real content

# Function to get sentiment from VADER
def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    st.write("📊 VADER Scores:", scores)

    compound = scores['compound']
    if compound >= 0.5:
        return "Positive"
    elif compound <= -0.5:
        return "Negative"
    else:
        return "Neutral"

# Input text area
tweet = st.text_area("✍️ Enter a tweet", value=st.session_state.text_input)

# Predict button
if st.button("🔍 Predict Sentiment"):
    if tweet.strip() and is_valid_tweet(tweet):
        st.session_state.text_input = tweet
        sentiment = get_sentiment(tweet)
        if sentiment == "Positive":
            st.success("😊 Positive Sentiment Detected!")
        elif sentiment == "Negative":
            st.error("😡 Negative Sentiment Detected!")
        else:
            st.info("😐 Neutral Sentiment Detected.")
    else:
        st.warning("⚠️ Please enter a meaningful tweet (not just symbols).")

# Clear button
if st.button("🧹 Clear"):
    st.session_state.text_input = ""
    st.query_params.clear()
    st.stop()

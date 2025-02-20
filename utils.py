from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive 😊", "positive"
    elif sentiment < 0:
        return "Negative 😔", "negative"
    else:
        return "Neutral 😐", "neutral"

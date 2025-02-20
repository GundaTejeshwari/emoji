import pickle
from utils import analyze_sentiment

# Save the function using pickle
with open("sentiment_model.pkl", "wb") as file:
    pickle.dump(analyze_sentiment, file)

print("Sentiment analysis model saved as 'sentiment_model.pkl'")

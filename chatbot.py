import requests
import streamlit as st
import random

# Giphy API key (replace with your actual key)
GIPHY_API_KEY = "QxgEXEdR8ulaKP5vTM6zIIQnmdF30w57"

def get_gif_url(query):
    """
    Fetch a GIF URL from Giphy based on the user's query.
    """
    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": GIPHY_API_KEY,
        "q": query,
        "limit": 10,  # Fetch up to 10 GIFs to allow random selection
        "offset": 0,
        "rating": "G",  # General audience
        "lang": "en",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["data"]:
            # Select a random GIF from the results
            gif_data = random.choice(data["data"])
            return gif_data["images"]["original"]["url"]  # Return the direct GIF URL
    return None  # Return None if no GIFs are found

# Streamlit UI
st.title("Dynamic GIF Chatbot")
st.write("Enter your message below, and get a relevant GIF:")

# Chat input
user_input = st.text_input("You:", "")

if user_input:
    # Fetch a GIF based on user input
    gif_url = get_gif_url(user_input)
    
    # Display GIF or fallback message
    if gif_url:
        st.image(gif_url, caption="Here's a GIF for your message!", use_column_width=True)
    else:
        st.write("No GIF found for your input. Try a different message!")
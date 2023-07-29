import streamlit as st
import requests

# Prepare API key and URL
api_key = "wUFHJpE5dN4kju8zxCJblCV1g8AlNW5PgMYkXOJt"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the request data as dictionary
response = requests.get(url)
content = response.json()

# Extract the title, image and explanation
title = content["title"]
img_url = content["url"]
explanation = content["explanation"]

# Download the image
img_filepath = "image.jpg"
img_response = requests.get(img_url)
img_content = img_response.content
with open(img_filepath, "wb") as file:
    file.write(img_content)

# Adding the data to the web page
st.header(title)
st.image("image.jpg")
st.info(explanation)
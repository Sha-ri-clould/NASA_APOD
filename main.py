import requests
import streamlit as st
import datetime
import os

API_key = os.getenv("API_KEY")
st.set_page_config(layout="wide",page_title="NASA Astronomy Picture of the day")
today = datetime.date.today()

st.title("Astronomy Picture of the Day")
st.markdown("*Every day, the universe has a new story to tell, View NASA’s daily astronomy image.*")
date = st.date_input("Pick a date",today)
submit= st.button("Submit")


response = requests.get("https://api.nasa.gov/planetary/apod?"
                        f"start_date={date}&end_date={date}&"
                        f"""api_key={API_key}""")
contents = response.json()
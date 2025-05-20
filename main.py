import requests
import streamlit as st
import datetime
import os

API_key = os.getenv("NASA_API_key")
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

if submit:
    for content in contents:
        if content["media_type"] == "image":
            st.subheader(f"""{content["title"]} - {date}""")
            img= requests.get(content["hdurl"])
            with open("nasa_apod.jpg","wb") as file:
                file.write(img.content)
                st.image("nasa_apod.jpg")
            st.subheader("Let's Dive Deeper!")
            st.text(content["explanation"])

        else:
            st.error("PICK ANOTHER DATE")
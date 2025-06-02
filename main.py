import requests
import streamlit as st
import datetime
import os

API_key = "j0hKNx9RO5xwHzbckQp6Dpgp57YIV0CPqZ2qlHiZ"
st.set_page_config(layout="wide",page_title="NASA Astronomy Picture of the day")
start_date = "1995-06-16"
today = datetime.date.today()

st.title("Astronomy Picture of the Day")
st.markdown("*Every day, the universe has a new story to tell, View NASA’s daily astronomy image.*")
date = st.date_input("Pick a date",value=today,min_value=start_date,max_value=today)
submit= st.button("Submit")


response = requests.get("https://api.nasa.gov/planetary/apod?"
                        f"start_date={date}&end_date={date}&"
                        f"""api_key={API_key}""")
contents = response.json()

for content in contents:
    if content["media_type"] == "image":
        st.subheader(f"""{content["title"]} - {date}""")
        img = requests.get(content["hdurl"])
        with open("nasa_apod.jpg", "wb") as file:
            file.write(img.content)
            st.image("nasa_apod.jpg")
        st.subheader("Let's Dive Deeper!")
        st.text(content["explanation"])

    else:
        st.error("PICK ANOTHER DATE")

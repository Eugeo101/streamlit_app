## inputs
import streamlit as st
import datetime
num_1 = st.number_input(label="salary", min_value=0, max_value=1000) # input number
text_1 = st.text_input(label="product type", max_chars=1000, type="default")# input text
text_2 = st.text_input(label="password", max_chars=1000, type="password")# input text

min_date = datetime.datetime(year=2000, month=1, day=1)
date_1 = st.date_input(label='order date', min_value=min_date) # input date
time_1 = st.time_input(label="order-time") # input time
color = st.color_picker(label="pick a color") # color input
description = st.text_area(label="describiton") # text_area
file = st.file_uploader(label="upload your cv") # file uploader
submit = st.button(label="Submit")
if submit:
    print(num_1)
    print(text_1)
    print(text_2)
    print(date_1)
    print(time_1)
    print(color)
    print(description)
    print(file)
    print(file.read())
    # model.predict()

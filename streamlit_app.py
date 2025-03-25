import streamlit as st

# Title of the app
st.title("🎈 My Interactive Web App")

# Text input for user name
user_name = st.text_input("Enter your name:")

# Slider for selecting a number
number = st.slider("Select a number", 0, 100, 50)

# Button to submit the input
if st.button("Submit"):
    st.write(f"Hello, {user_name}! You selected the number {number}.")
else:
    st.write("Please enter your name and select a number.")

# Additional interactive element: Checkbox
if st.checkbox("Show more options"):
    st.write("You can add more features here!")
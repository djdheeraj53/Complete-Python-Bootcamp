import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, Sonali! Welcome to the Streamlit app.")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a simple text.")

if st.button("Greet me"):
    st.write("Hi! ")

agreement = st.checkbox("I agree to the terms and conditions")
if agreement:
    st.write("Thank you for agreeing!")

level = st.slider("Select a value", 0, 100, 2)

st.write(f"selected Level: {level}")

st.file_uploader("Upload a file", type = ["pdf"])

name = st.text_input("Enter your name")
# need to know about the type of name variable
st.write(f"Type of name variable: {type(name)}")


st.write(name)


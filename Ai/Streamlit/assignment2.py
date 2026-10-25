import streamlit as st

price = st.text_input("Enter Product Price")
price = int(price)  # Convert the input to an integer
discount = st.slider("Select a value %", 0, 50, 0)
discount = int(discount)  # Convert the input to an integer 

if st.button("Calculate Discount"):
    after_discount = price - (price * discount / 100)
    st.write(f"Price after discount: {after_discount}")
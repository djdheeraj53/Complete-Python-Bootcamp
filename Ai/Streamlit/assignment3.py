import streamlit as st

name = st.sidebar.text_input("Product Name")
category = st.sidebar.selectbox("Select Product Category", ["Electronics", "Clothing", "Books", "Home & Kitchen"])
price = st.sidebar.number_input("Product Price")

if st.sidebar.button("Submit Product Details"):
    st.success("Product details submitted successfully!")
    st.write("Product Name:", name)
    st.write("Product Category:", category)
    st.write("Product Price:", price)

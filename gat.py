import streamlit as st
if "page" not in st.session_state:
    st.session_state.page = "signup"
def navigate_to(page):
    st.session_state.page = page
if st.session_state.page == "signup":
    st.header("Sign Up")
    name = st.text_input("Enter Name")
    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", "password")
    if st.button("Submit"):
        if name and email and password:
            st.success("Sign up successful!")
        else:
            st.error("Please fill all fields.")
    if st.button("Already have an account? Login"):
        navigate_to("signin")
elif st.session_state.page == "signin":
    st.header("Sign In")
    signin_email = st.text_input("Enter Email")
    signin_password = st.text_input("Enter Password", "password")
    if st.button("Sign In"):
        if signin_email and signin_password:
            if signin_email == "test@example.com" and signin_password == "password":
                st.success("Sign in successful!")
            else:
                st.error("Invalid email or password.")
        else:
            st.error("Please enter email and password.")
    if st.button("Don't have an account? Sign Up"):
        navigate_to("signup")
        
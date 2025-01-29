import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "signup"

def navigate_to(page):
    st.session_state.page = page
if st.session_state.page == "signup":
    st.header("Sign Up")
    username = st.text_input("Enter UserName")
    name = st.text_input("Enter Name")
    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")
    countries = [
    "India", "China", "United States", "Indonesia", "Pakistan", "Nigeria", "Brazil",
    "Bangladesh", "Russia", "Ethiopia", "Mexico", "Japan", "Egypt", "Philippines",
    "DR Congo", "Vietnam", "Iran", "Turkey", "Germany", "Thailand", "United Kingdom",
    "Tanzania", "France", "South Africa", "Italy", "Kenya", "Myanmar", "Colombia",
    "South Korea", "Sudan", "Uganda", "Spain", "Algeria", "Iraq", "Argentina",
    "Afghanistan", "Yemen", "Canada", "Poland", "Morocco", "Angola", "Ukraine",
    "Uzbekistan", "Malaysia", "Mozambique", "Ghana", "Peru", "Saudi Arabia",
    "Madagascar", "Côte d'Ivoire", "Nepal", "Cameroon", "Venezuela", "Niger",
    "Australia", "North Korea", "Syria", "Mali", "Burkina Faso", "Sri Lanka",
    "Malawi", "Zambia", "Kazakhstan", "Chad", "Chile", "Romania", "Somalia",
    "Senegal", "Guatemala", "Netherlands", "Ecuador", "Cambodia", "Zimbabwe",
    "Guinea", "Benin", "Rwanda", "Burundi", "Bolivia", "Tunisia", "South Sudan",
    "Saint Kitts & Nevis", "Liechtenstein", "Monaco", "Marshall Islands", "San Marino",
    "Palau", "Nauru", "Tuvalu"
]
    country = st.selectbox("Select Country", countries)  
    if st.button("Submit"):
        if name and email and password and country:  
            st.success("Sign up successful!")
        else:
            st.error("Please fill all fields, including country.") 
    if st.button("Already have an account? Login"):
        navigate_to("signin")
elif st.session_state.page == "signin":
    st.header("Sign In")
    signin_email = st.text_input("Enter Email")
    signin_password = st.text_input("Enter Password", type="password")
    if st.button("Sign In"):
        if signin_email and signin_password:
            if signin_email == "test@example.com" and signin_password == "password":
                st.error("Sign in successful!")
            else:
                st.success("Invalid email or password.")
        else:
            st.error("Please enter email and password.")
    if st.button("Don't have an account? Sign Up"):
        navigate_to("signup")
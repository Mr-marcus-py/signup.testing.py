import streamlit as st

family_data = {}

def add_member():
    name = st.text_input("Name")
    relationship = st.text_input("Relationship (e.g., parent, child, spouse)")
    age = st.text_input("Age:")  
    gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])

    if st.button("Add Member"):
        if name and relationship and age and gender: 
            family_data[name] = {"relationship": relationship, "age": age, "other_info": gender}
            st.success(f"{name} added to the family!")
        else:
            st.error(" Please Fill all field.")
st.sidebar.write("---")
st.title(  " D.OLUWAREMI`S")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:  
    st.image("family.jpg", width=200)
st.write("---")    
st.subheader("**SIGN UP!**")
st.sidebar.header("Family Actions")
add_member()
st.sidebar.write("---")



# Main display area
# display_family()
import streamlit as st

# Family data (you can customize this)
family_members = {
    "Father": {"name": "John", "age": 50},
    "Mother": {"name": "Jane", "age": 45},
    "Son": {"name": "Mike", "age": 20},
    "Daughter": {"name": "Sarah", "age": 15},
    "Grandmother": {"name": "Mary", "age": 75}  # Example of adding another member
}

# Streamlit app
st.title("Welcome to the Family Dashboard!")

# Display family members' information
st.header("Family Members")

# Method 1: Using st.write and f-strings (more flexible for formatting)
for relationship, details in family_members.items():
    st.write(f"**{relationship}:** {details['name']} ({details['age']} years old)")


# Method 2: Using a Pandas DataFrame (good for tabular data)
import pandas as pd

family_data = []
for relationship, details in family_members.items():
    family_data.append({"Relationship": relationship, "Name": details["name"], "Age": details["age"]})

df = pd.DataFrame(family_data)
st.dataframe(df)  # Or st.table(df) for a static table


# Add some styling (optional)
st.markdown("""
<style>
body {
    font-family: sans-serif;
}
.family-member {
    margin-bottom: 10px;
}
.relationship {
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)  # Note: unsafe_allow_html is generally discouraged for production apps, but okay for simple personal dashboards.

# Example of adding an image (optional)
# from PIL import Image  # Make sure you have Pillow installed: pip install Pillow
# image = Image.open("family_photo.jpg") # Replace with your image path
# st.image(image, caption="Our Family", use_column_width=True)


# Add a family quote or message (optional)
st.subheader("A Family Thought")
st.write('"Family is not an important thing. It\'s everything." - Michael J. Fox')


# Interactive element (optional): Age input and greeting
st.subheader("Personalized Greeting")
name_input = st.text_input("Enter your name:")
if name_input:
    st.write(f"Hello, {name_input}! Welcome to the family dashboard.")

age_input = st.number_input("Enter your age:", min_value=0, value=25, step=1)  # Default age 25
st.write(f"Your age is: {age_input}")



# Run the app: streamlit run your_script_name.py (replace your_script_name.py)
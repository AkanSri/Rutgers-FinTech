# @TODO: Import the libraries for Pandas and Streamlit
import streamlit as st
import pandas as pd

# @TODO: Create a title for your application using markdown syntax and the
# Streamlit `write` function.
st.write("# Python Web App")


# @TODO: Create an opening sentence for your application using regular text and
# the Streamlit `write` function.
st.write("Hi, this is our first web app in Python! :sunglasses:")

# @TODO: Create a Pandas dataframe
# @TODO: Write the Pandas dataframe to the page
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
st.write(df)




# @TODO: Create a text input box using the Streamlit `text_input` function.
# @TODO: Save the input as a variable.
input_value = st.text_input("Enter a Message")

# @TODO: Utilize the Streamlit `button` function to display the text input
# variable created in the prior step to the page.
if st.button("Display Message"):
    st.write(input_value)

# Bonus
# YOUR CODE HERE!

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("My Streamlit App")
st.write("This is a simple Streamlit application that displays a DataFrame and a Plotly chart.")

# Create a sample DataFrame
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# Display the DataFrame
st.write("### DataFrame")
st.dataframe(df)

# Create a Plotly chart
fig = px.bar(df, x="Category", y="Values", title="Sample Bar Chart")
st.plotly_chart(fig)

st.write("### End of the App")

st.write("Thank you for using the app!")
# Run the app with: streamlit run app.py
st.write("Feel free to modify the code and explore Streamlit features!")
st.write("### End of the App")
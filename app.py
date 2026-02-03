import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Vehicles Web App")
st.write("This is a simple Streamlit application that displays some useful graphics about vehicle information.")

# Imorting vehicle data
vehicles = pd.read_csv("/Users/jking/Data_Science/Sprint4Project/vehicles_us.csv")

#---------------Display the DataFrame---------------
st.write("### Preview of Vehicle Data")
st.dataframe(vehicles)
#-----------------------------------------------------------

st.write("### Start of App")

#--------------- Histogram ---------------

fig1 = px.histogram(
    vehicles,
    x='price',
    nbins=50,
    title="Distribution of Vehicle Prices",
    labels={"price": "Price of Vehicles(in USD)"}
)
#fig1.show()
st.plotly_chart(fig1, use_container_width=True) #auto resizes chart

#-----------------------------------------
#---------------Price vs Mileage Scatter Plot ---------------
#conditions in order(worst to best)
quality_order=['salvage', 'fair','good','excellent', 'like new', 'new'] 

# make condition ordered categorical
vehicles['condition'] = pd.Categorical(
    vehicles['condition'],
    categories=quality_order,
    ordered=True
)
#color scheme based on condition
semantic_colors = st.checkbox("Use semantic colors (bad->good)")
default_palette = px.colors.qualitative.D3
semantic_palette = ['#d62728', '#ff7f0e', '#bcbd22', '#2ca02c', '#17becf', '#1f77b4'] #red to blue-green
palette = semantic_palette if semantic_colors else default_palette

fig2 = px.scatter(
    vehicles, 
    x='odometer', 
    y='price', 
    color='condition',
    opacity=0.3,
    category_orders={'condition': quality_order[::-1]}, #reverse order for legend (best on top)
    color_discrete_sequence=palette,
    title="Price vs Mileage Scatter Plot",
    labels={"odometer": "Mileage", "price": "Price of Vehicles(in USD)"})
fig2.update_xaxes(tickformat=",")
#fig2.show()
st.plotly_chart(fig2, use_container_width=True) #auto resizes chart


#--------------- Vehicle Condition Bar Chart ---------------

#create a 2 column dataframe based on condition and count
condition_df = vehicles['condition'].value_counts().sort_index().reset_index()
condition_df.columns = ['condition', 'count']
print(condition_df)

reverse_condition = st.checkbox("Reverse Order of Condition (best -> worst)")
order = quality_order[::-1] if reverse_condition else quality_order #if check box activated reverse order
fig3 = px.bar(
    condition_df, 
    category_orders={'condition': order}, 
    x='condition',
    y='count', 
    labels={"condition": "Condition","count": "Number of Vehicles"}, 
    title="Vehicle Condition")
#fig3.show()
st.write("Number of vehicles found in each condition")
st.plotly_chart(fig3, use_container_width=True) #auto resizes chart
#-------------------------------------------------------------
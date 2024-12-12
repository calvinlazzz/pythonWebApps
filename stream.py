import streamlit as st
import pandas 
#https://streampy-lyb687r95y7kejkesfm5e7.streamlit.app/
data = {
    'Series_1': [1, 2, 3, 4, 5],
    'Series_2': [10, 20, 30, 40, 50]
}

df = pandas.DataFrame(data)

st.title('Streamlit App')
st.subheader('This is a subheader')
st.write('This is a normal text')
st.write(df)
st.line_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', (myslider * 9/5) + 32)
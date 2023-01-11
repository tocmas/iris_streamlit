import streamlit as st
import numpy as np
import pandas as pd

st.title("streamlit 基礎")
st.write("hello World!")

df=pd.DataFrame({
    "1列目" : [1,2,3,4],
    "2列目" : [10,20,30,40]
})

st.dataframe(df)

st.dataframe(df.style.hightlight_max(axis=0),width=100,height=150)

df = pd.DataFrame(
    np.random.rand(10,3),
    columns = ['a', 'b', 'c'])
    
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
    
df = pd.DataFrame(
    np.random.rand(100,2) / [50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon'])
    
st.map(df)

img = Image.open('Iris.jpg')
st.image(img,caption = 'Iris' , use_column_width = True)

if st.checkbox('Show Image'):
    img = Image.open('iris.jpg')
    st.image(img,caption = 'Iris' , use_column_width = True)
    
option = st.selectbox(
    '好きな数字を入力してください。',
    list(range(1, 11))
)

'あなたの好きな数字は' , option , 'です。'
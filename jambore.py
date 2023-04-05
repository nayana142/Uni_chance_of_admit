import streamlit as st
import pandas as pd
st.title('Jamboree Admission')
st.write('''
Simple jamboree admission  app
''')

st.sidebar.header('User input parameters')
def user_input_features():
    GRE_Score= st.sidebar.slider('GRE Score', 290, 340, 300)
    TOEFL_Score = st.sidebar.slider('TOEFL Score', 92,120, 100)
    University_Rating = st.sidebar.slider('University Rating', 1, 5, 3)
    SOP = st.sidebar.slider('SOP', 1.0,5.0,3.0)
    LOR = st.sidebar.slider('LOR ', 1.0,5.0,3.0)
    CGPA = st.sidebar.slider('CGPA', 6.8, 9.92, 8.2)
    Research = st.sidebar.slider('Research', 0.1, 1.0,0.5)


    data = {'GRE Score': GRE_Score,
            'TOEFL Score': TOEFL_Score,
            'University Rating': University_Rating,
            'SOP': SOP,
            'LOR ': LOR,
            'CGPA': CGPA,
            'Research': Research,
            }
    features = pd.DataFrame(data, index=[0])
    return features
df= user_input_features()

st.subheader("User Input Parameters")
st.write(df)

jamboree = pd.read_csv('Jamboree_Admission1.csv')
# jamboree=jamboree.rename(columns={'Chance of Admit':'Chance of Admit'})
x = jamboree.drop(['Chance of Admit ','Serial No.'],axis=1)
y = jamboree['Chance of Admit ']
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x1=scaler.fit_transform(x)
x1=pd.DataFrame(x1,columns=x.columns)

from sklearn.linear_model import LinearRegression
from sklearn import metrics
model = LinearRegression()
model.fit(x1,y)

## prediction
prediction =model.predict(df)
ds=pd.DataFrame()
ds.rename({'0':'predicted_chance_admit'})

st.subheader('Prediction')
st.write(prediction)
st.subheader(' Actual chance of Admit')

st.write(jamboree['Chance of Admit '])




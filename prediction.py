
import pandas as pd
import streamlit as st
import pickle

filename = "Log Reg Building Insurance.sav"
model = pickle.load(open(filename, 'rb')) 

st.title ('My SIWES PROJECT REPORT')
st.title ('Building insurance Claim app')
st.subheader('This app takes in certain variable to enable prediction')


def user_imput():
    YearObservation = st.slider('what year was your building insured', 2012, 2016)
    Insured_Period = st.slider('what is the duration of the insurance?',0, 10)
    Residential = st.selectbox('is the buidling residential or not hint 1 for yes and 0 for no', options = [0,1], index = 0)
    Garden = st.selectbox('Does the building has a Graden or not hint 1 for yes and 0 for no', options = [0,1], index = 0)
    building_fenced = st.selectbox('is the buidling fenced or not', options = [0,1], index = 0)
    building_painted = st.selectbox('is the buidling painted or not', options = [0,1], index = 0)
    settlement = st.selectbox('is the area rural or urban', options = [0,1], index = 0)
    Building_dimension =  st.slider('what is the dimension of your bulding', 1.0, 30000.0)
    Building_Type = st.selectbox('what is your building type', options = [0,1,2,3], index = 0)
    Date_of_Occupancy = st.slider('Date of occupancy', 1545, 2016)
    Number_of_window = st.slider('Number of Window', 0, 20)
    Geo_code = st.slider('Geographical code of the building?', 0, 2000)
    #page = st.sidebar.selectbox("Choose a page", options  = [1, 2, 3])


    data = {'YearOfObservation':YearObservation,
            'Insured_Period': Insured_Period,
            'Residential': Residential,
            'Building_Painted': building_painted,  
            'Building_Fenced': building_fenced,
            'Garden': Garden,
            'Settlement': settlement,
            'Building Dimension': Building_dimension,
            'Building_Type': Building_Type,
            'Date_of_Occupancy': Date_of_Occupancy,
            'NumberOfWindows': Number_of_window,
            
            'Geo_Code': Geo_code
            #'page':page
           
           
           }

    features = pd.DataFrame(data, index=[0])  #- convert the dictionary to dataframe
    
    return features

df = user_imput()



def prediction():
    predict = model.predict(df)
    result = ''
    if predict == 0:
        result = 'Not Qualified'
    else:
        result= 'Qualified'
    return result


submit = st.button('Get prediction')
result = prediction()
if submit:
    st.success('Thank you for filling the form. you are {}'.format(result))


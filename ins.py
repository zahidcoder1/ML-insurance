# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import joblib

def main():
    html_temp="""
    <div style="background-color:lightblue; padding:16px">
    <h2 style="color:black"; text-align:center>Insurance Cost Prediction</2>
    </div>
    
    """
    
    
    st.markdown(html_temp, unsafe_allow_html=True)
    
    model= joblib.load("model_joblib_gr")

    p1=st.slider("Enter your age:",18,100)
    
    s1 = st.selectbox("age:",("male","female"))
    if s1=="male":
        p2=p1
    else:
        p2=0
    
    p3 = st.number_input("Enter your bmi:")
    
    p4 = st.slider("Enter number of children:",0,4)
    
    s2 = st.selectbox("Smoker",("Yes","No"))
    if s2=="Yes":
        p5=1 
    else:
        p5=0
    
    p6 = st.slider("Enter your Region:",1,4)
    
    if st.button("Predict"):
        pred=model.predict([[p1,p2,p3,p4,p5,p6]])
        
        st.success("Your insurance cost is {}".format(round(pred[0],2)))
        
if __name__=='__main__':
    main()
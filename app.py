import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

with open("C:\Users\prane\OneDrive\Desktop\api key.txt", "r") as file:
    api_key = file.read().strip() 


## streamlit UI
st.set_page_config(page_title="Travel Cost Estimator", layout="wide")
st.title('🚀AI Powered Travel Planner')
st.write('Enter your travel details to get the estimated costs for various travel modes')
st.markdown("### Enter Source and Destination to Get Travel Details:")

## user input fields
source = st.text_input('Enter Source location')
destination = st.text_input('Enter the Destination location')

if st.button('Estimate Travel Details:'):
    if source and destination:
        ## langchain components
        ## logic1: template
        chat_template = ChatPromptTemplate(messages=
            [ ("system", """
                You are a structured AI travel assistant. Your task is to generate a Markdown table summarizing travel options. 
                
                ### **Table Columns**:
                - Mode of Transport
                - Distance
                - Duration
                - Estimated Cost (₹)
                - Pros
                - Cons
                **Output only a Markdown table** without extra text. 
                Replace "X" with actual travel details.
            """),
               ("human","""Plan a trip from {source} to {destination}.""")]
        )
        ## logic2: model
        chat_model = ChatGoogleGenerativeAI(api_key= api_key, model="gemini-2.0-flash-exp")
        ## logic3: output parsing
        parser = StrOutputParser()
        ## chain
        chain = chat_template | chat_model | parser

        raw_input = {"source":source,"destination":destination}
        response = chain.invoke(raw_input)
        st.subheader("Travel Plan Details:")
        st.markdown(response, unsafe_allow_html=True)

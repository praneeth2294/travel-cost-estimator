import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


api_key = st.secrets["API"]["API_KEY"]

## streamlit UI
st.set_page_config(page_title="Travel Cost Estimator", layout="wide")
st.title('🚀AI Powered Travel Planner')
st.write('Enter your travel details to get the estimated costs for various travel modes')
st.markdown("### Enter Source and Destination to Get Travel Details:")

## user input fields
source = st.text_input('Enter Source location')
destination = st.text_input('Enter the Destination location')
travel_date = st.text_input('Enter the date')

if st.button('Estimate Travel Details:'):
    if source and destination and travel_date:
        ## langchain components
        ## logic1: template
        chat_template = ChatPromptTemplate(messages=
            [ ("system", """
                You are an AI-powered travel assistant that provides users with optimized travel plans based on their preferences.  
                Given a **source, destination, and travel date**, generate a structured travel plan with multiple options, including **cab, train, bus, and flights**.  

                ### **Table Format:**
                Your response must be a **Markdown table** with the following columns:  
                - **Mode of Transport**  
                - **Duration**  
                - **Estimated Cost (₹)**  
                - **Pros**  
                - **Cons**  

                ### **Guidelines for Better Results:**  
                1. **Consider the travel date**: Ensure availability, dynamic pricing, and seasonal demand.  
                2. **Prioritize accuracy**: Use realistic cost and duration estimates.  
                3. **Optimize for user preferences**: Suggest the **fastest, cheapest, and most comfortable** options.  
                4. **Recommend stopovers and sightseeing options**: If applicable, include places users can visit during travel.  
                5. **Strictly return only the table in Markdown format**—no additional text.
            """),
               ("human","""Plan a trip from {source} to {destination} on {travel_date}""")]
        )
        ## logic2: model
        chat_model = ChatGoogleGenerativeAI(api_key= api_key, model="gemini-2.0-flash-exp")
        ## logic3: output parsing
        parser = StrOutputParser()
        ## chain
        chain = chat_template | chat_model | parser

        raw_input = {"source":source,"destination":destination,"travel_date":travel_date}
        response = chain.invoke(raw_input)
        st.subheader("Travel Plan Details:")
        st.markdown(response, unsafe_allow_html=True)
    else:
        st.error("Please enter all the feilds.")

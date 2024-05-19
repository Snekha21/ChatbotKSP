## loading all the environment variables
import streamlit as st
import os
import google.generativeai as genai
import streamlit as st
genai.configure(api_key="AIzaSyA3pzFiHktKXSwOhnSsLzEE6dNJb-QptI8")

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
st.set_page_config(layout="wide",page_title="VISION PRO")
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.header('VISION BOT')


st.markdown(hide_default_format, unsafe_allow_html=True)

st.write("Features of this chatbot")
st.markdown("- Emergency Reporting")
st.markdown("- Information Retrieval")
st.markdown("- Multi-language Support")
st.markdown("- Integration with Emergency Services")
st.markdown("- Status Updates")
st.markdown("- Language Translation")
st.markdown("- Mental Health and Counseling Support")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="VISION PRO CHATBOT")

st.header("VISION PRO CHATBOT")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
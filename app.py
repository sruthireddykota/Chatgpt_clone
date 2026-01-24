import os
import streamlit as st
from streamlit_chat import message
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

if 'conversation' not in st.session_state:
    st.session_state['conversation'] = None
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'API_Key' not in st.session_state:
    st.session_state['API_Key'] = ''
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = InMemoryChatMessageHistory()
    
st.set_page_config(page_title="Chat GPT Clone", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>How can I assist you? </h1>", unsafe_allow_html=True)
st.sidebar.title("😎")
st.session_state['API_Key'] = st.sidebar.text_input("What's your API key?", type="password")
summarise_button = st.sidebar.button("Summarise the conversation", key="summarise")
if summarise_button:
    if st.session_state['chat_history'].messages:
        summary = "\n\n".join([f"{'User' if i % 2 == 0 else 'AI'}: {msg.content}" 
                               for i, msg in enumerate(st.session_state['chat_history'].messages)])
        st.sidebar.write("Nice chatting with you my friend ❤️:\n\n" + summary)
def getresponse(userInput, openai_api_key):
    if st.session_state['conversation'] is None:
        llm = AzureChatOpenAI(
            azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"],       
            openai_api_key=openai_api_key,
            openai_api_version="2024-06-01",
            deployment_name=st.secrets["AZURE_OPENAI_DEPLOYMENT"], 
            temperature=0.9
        )
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI assistant."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])
        chain = prompt | llm
        
        st.session_state['conversation'] = RunnableWithMessageHistory(
            chain,
            lambda session_id: st.session_state['chat_history'],
            input_messages_key="input",
            history_messages_key="history"
        )

    response = st.session_state['conversation'].invoke(
        {"input": userInput},
        config={"configurable": {"session_id": "default"}}
    )
    
    return response.content

response_container = st.container()
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("Your question goes here:", key='input', height=100)
        submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            st.session_state['messages'].append(user_input)
            model_response = getresponse(user_input, st.session_state['API_Key'])
            st.session_state['messages'].append(model_response)
            
            with response_container:
                for i in range(len(st.session_state['messages'])):
                    if (i % 2) == 0:
                        message(st.session_state['messages'][i], is_user=True, key=str(i) + '_user')
                    else:
                        message(st.session_state['messages'][i], key=str(i) + '_AI')
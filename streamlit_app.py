import streamlit as st
from gpt4all import GPT4ALL

model = GPT4ALL("GPT4All-13B-snoozy.ggmlv3.q4_0.bin")

# Storage
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for message in st.session_state.messages:
    with st.chat_message(message.get("role")):
        st.write(message.get("content"))

prompt = st.chat_input("Ask something about TIP!")

if prompt:
    # Add to storage
    st.session_state.messages.append({"role": "user","content":prompt})
    
    # Display message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Process response
    result = model.chat_completion({"role": "assistant","content":prompt})
    response = result["choices"][0]["message"]["content"]
    
    # Store response
    st.session_state.messages.append({"role": "assistant","content":response})

    # Display response
    with st.chat_message("assistant"):
        st.markdown(response)

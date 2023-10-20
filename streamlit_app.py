import streamlit as st

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

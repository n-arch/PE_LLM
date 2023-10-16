import streamlit as st
import json
import os
from models import peEntry





# Dummy chatbot function
def chatbot_response(text):
    return f"You said: {text}"


st.title('PE Anweisungen')


st.markdown("""Bei der Dokumentation eines geplanten Ereignisses stellen Sie bitte sicher, dass Sie umfassende Details in den folgenden Bereichen bereitstellen:\n

Titel: Geben Sie den genauen Titel des Ereignisses deutlich an. Dies wird der Hauptidentifikator für alle zugehörigen Diskussionen und Dokumentationen sein.\n
Zustand vorher: Beschreiben Sie detailliert die aktuelle Situation oder den Zustand vor dem Ereignis. Dies hilft, die Notwendigkeit und die Auswirkungen der vorgeschlagenen Änderung zu bewerten.\n
Zustand nachher: Geben Sie Einblicke in den erwarteten Zustand oder die Situation nach dem Ereignis. Dies bietet eine Prognose über die Vorteile und Auswirkungen der Änderung.\n
Begründung: Erklären Sie die Gründe für die Durchführung dieses Ereignisses. Wenn die Gründe zu allgemein erscheinen oder nicht detailliert sind, kann eine weitere Klärung angefordert werden. Es ist wichtig, hier spezifisch zu sein, um Unklarheiten zu vermeiden.\n
Auslöser: Geben Sie an, was genau dieses Ereignis auslöst oder initiiert. Wenn der Auslöser nicht sofort klar ist oder nicht angegeben wird, seien Sie bitte bereit, auf Anfrage zusätzliche Informationen bereitzustellen.\n
Rationale: Geben Sie an, ob für dieses Ereignis ein Effizienzcheck erforderlich ist, und begründen Sie dies klar. Dies hilft, die tieferen Ziele und die strategische Bedeutung des Ereignisses zu verstehen.""")

st.title('PE Chatbot')


# Window 1
# Initialize conversation history if not already done
if 'chat_history_1' not in st.session_state:
    st.session_state.chat_history_1 = []

# Text input for the user's message
user_input_1 = st.text_area("Title")

if st.button("Send 1"):
    # Add user message to chat history
    st.session_state.chat_history_1.append(("You:", user_input_1))
    
    # Get bot's response and add to chat history
    bot_response = peEntry.chat_title(user_input_1)
    st.session_state.chat_history_1.append(("Bot:", bot_response))
    
    st.session_state.text_area_content = ""

if st.button('Clear 1'):
    st.session_state.chat_history_1 = []

# Reset button
if st.button('Reset 1'):
    st.session_state.chat_history_1 = []
    st.experimental_rerun()

# Display chat history
for user, text in st.session_state.chat_history_1:
    if user == "You:":
        st.write(f"**{user}** {text}")
    else:
        st.write(f"{user} {text}")

# Window 2
# Initialize conversation history if not already done
if 'chat_history_2' not in st.session_state:
    st.session_state.chat_history_2 = []

# Text input for the user's message
user_input_2 = st.text_area("State Before")

if st.button("Send 2"):
    # Add user message to chat history
    st.session_state.chat_history_2.append(("You:", user_input_2))
    
    # Get bot's response and add to chat history
    bot_response = peEntry.chat_state_before(user_input_2)
    st.session_state.chat_history_2.append(("Bot:", bot_response))
    
    st.session_state.text_area_content = ""

if st.button('Clear 2'):
    st.session_state.chat_history_2 = []

# Reset button
if st.button('Reset 2'):
    st.session_state.chat_history_2 = []
    st.experimental_rerun()

# Display chat history
for user, text in st.session_state.chat_history_2:
    if user == "You:":
        st.write(f"**{user}** {text}")
    else:
        st.write(f"{user} {text}")

# Window 3
# Initialize conversation history if not already done
if 'chat_history_3' not in st.session_state:
    st.session_state.chat_history_3 = []

# Text input for the user's message
user_input_3 = st.text_area("State After")

if st.button("Send 3"):
    # Add user message to chat history
    st.session_state.chat_history_3.append(("You:", user_input_3))
    
    # Get bot's response and add to chat history
    bot_response = peEntry.chat_state_after(user_input_3)
    st.session_state.chat_history_3.append(("Bot:", bot_response))
    
    st.session_state.text_area_content = ""

if st.button('Clear 3'):
    st.session_state.chat_history_3 = []

# Reset button
if st.button('Reset 3'):
    st.session_state.chat_history_3 = []
    st.experimental_rerun()

# Display chat history
for user, text in st.session_state.chat_history_3:
    if user == "You:":
        st.write(f"**{user}** {text}")
    else:
        st.write(f"{user} {text}")

# Window 4
# Initialize conversation history if not already done
if 'chat_history_4' not in st.session_state:
    st.session_state.chat_history_4 = []

# Text input for the user's message
user_input_4 = st.text_area("Justification")

if st.button("Send 4"):
    # Add user message to chat history
    st.session_state.chat_history_4.append(("You:", user_input_4))
    
    # Get bot's response and add to chat history
    bot_response = peEntry.chat_justification(user_input_4)
    st.session_state.chat_history_4.append(("Bot:", bot_response))
    
    st.session_state.text_area_content = ""

if st.button('Clear 4'):
    st.session_state.chat_history_4 = []

# Reset button
if st.button('Reset 4'):
    st.session_state.chat_history_4 = []
    st.experimental_rerun()

# Display chat history
for user, text in st.session_state.chat_history_4:
    if user == "You:":
        st.write(f"**{user}** {text}")
    else:
        st.write(f"{user} {text}")

# Window 5
# Initialize conversation history if not already done
if 'chat_history_5' not in st.session_state:
    st.session_state.chat_history_5 = []

# Text input for the user's message
user_input_5 = st.text_area("Trigger")

if st.button("Send 5"):
    # Add user message to chat history
    st.session_state.chat_history_5.append(("You:", user_input_5))
    
    # Get bot's response and add to chat history
    bot_response = peEntry.chat_trigger(user_input_5)
    st.session_state.chat_history_5.append(("Bot:", bot_response))
    
    st.session_state.text_area_content = ""

if st.button('Clear 5'):
    st.session_state.chat_history_5 = []

# Reset button
if st.button('Reset 5'):
    st.session_state.chat_history_5 = []
    st.experimental_rerun()

# Display chat history
for user, text in st.session_state.chat_history_5:
    if user == "You:":
        st.write(f"**{user}** {text}")
    else:
        st.write(f"{user} {text}")

# Window 6
# Initialize conversation history if not already done
if 'chat_history_6' not in st.session_state:
    st.session_state.chat_history_6 = []

# Text input for the user's message
user_input_6 = st.text_area("Rationale")

if st.button("Send 6"):
    # Add user message to chat history
    st.session_state.chat_history_6.append(("You:", user_input_6))
    
    # Get bot's response and add to chat history
    bot_response = peEntry.chat_rationale(user_input_6)
    st.session_state.chat_history_6.append(("Bot:", bot_response))
    
    st.session_state.text_area_content = ""

if st.button('Clear 6'):
    st.session_state.chat_history_6 = []

# Reset button
if st.button('Reset 6'):
    st.session_state.chat_history_6 = []
    st.experimental_rerun()

# Display chat history
for user, text in st.session_state.chat_history_6:
    if user == "You:":
        st.write(f"**{user}** {text}")
    else:
        st.write(f"{user} {text}")





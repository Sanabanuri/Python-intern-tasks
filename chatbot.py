import json
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
gemini_key = os.getenv("MY_CHATBOT_KEY")
client = genai.Client(api_key=gemini_key)

chat = client.chats.create(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig(
        system_instruction='Your name is Mindwired. Answer very concisely.'
    )
)

print("-" * 45)
print("Mindwired CLI Chatbot (Type 'quit' to exit)")
print("-" * 45)

while True:
    user_input = input('You: ').strip()

    if not user_input:
        continue

    if user_input.lower() == 'quit':
        print("Saving conversation...")
        
        history = chat.get_history()
        
        chat_data = []
        for entry in history:
            chat_data.append({
                "sender": entry.role,
                "message": entry.parts[0].text
            })
            print(f"{entry.role} : {entry.parts[0].text}")
        
        with open("chat_log.json", "w") as f:
            json.dump(chat_data, f, indent=4)
            
        print("Chat saved to chat_log.json. Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print(f"Mindwired: {response.text}")
    except Exception as e:
        print(f"Error occurred: {e}")
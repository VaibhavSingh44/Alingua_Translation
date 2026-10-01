import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
#
# for model in client.models.list():
#     print(model.name)

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Explain AI in simple terms"
# )
#
# print(response.text)

def translate_text(input_text, selected_source_language, selected_target_language):
    prompt = f""" translate the following language from {selected_source_language} to {selected_target_language}: {input_text}"""

    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = prompt
    )
    return response.text

@st.cache_data
def translate_cached(input_text, selected_source_language, selected_target_language):
    return translate_text(input_text, selected_source_language, selected_target_language)

st.set_page_config(page_title = "AI-Powered Language Translator")
st.header("AI-Powered Language Translator")

text = st.text_area("Enter text here", placeholder = "type something to translate")
source_language = st.selectbox("Select Source Language", ["English", "Spanish", "French", "German", "Chinese"])
target_language = st.selectbox("Select Target Language", ["English", "Spanish", "French", "German", "Chinese"])

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter a text")
    else:
        translated_text = translate_cached(text, source_language, target_language)
        st.subheader('Translated_Text:')
        st.write(translated_text)


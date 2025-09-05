import requests
import streamlit as st 

def get_openai_response(input_text):
    try:
        response = requests.post("http://localhost:8000/essay/invoke",
                                json={'input': {'topic': input_text}})
        print("OpenAI Response Status:", response.status_code)
        print("OpenAI Response Text:", response.text)
        return response.json()['output']['content']
    except requests.exceptions.JSONDecodeError as e:
        print("JSONDecodeError:", str(e))
        print("Response Content:", response.text)
        return f"Error: Unable to parse response - {response.text}"
    except requests.exceptions.RequestException as e:
        print("Request Error:", str(e))
        return f"Error: Request failed - {str(e)}"

def get_ollama_response(input_text):
    try:
        response = requests.post("http://localhost:8000/poem/invoke",
                                json={'input': {'topic': input_text}})
        print("Ollama Response Status:", response.status_code)
        print("Ollama Response Text:", response.text)
        return response.json()['output']['content']
    except requests.exceptions.JSONDecodeError as e:
        print("JSONDecodeError:", str(e))
        print("Response Content:", response.text)
        return f"Error: Unable to parse response - {response.text}"
    except requests.exceptions.RequestException as e:
        print("Request Error:", str(e))
        return f"Error: Request failed - {str(e)}"

st.title('Essay and Poem Generator')
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))
if input_text1:
    st.write(get_ollama_response(input_text1))
import os
import requests

class QAEngine:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = os.getenv("GROQ_API_URL")
        self.model = "meta-llama/llama-4-maverick-17b-128e-instruct"

    def ask_about_celebrity(self, name, question):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        prompt = f""" You are a AI Assistant that knows a lot about celebrities. You have to answer questions about {name} concise and accurately.
        Question: {question}"""

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                    
                }
            ],
            "temperature": 0.3,
            "max_tokens": 1024
        }

        response = requests.post(self.api_url, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()['choices'][0]['message']['content']
            return result

        return "Sorry,I don't know about this celebrity."
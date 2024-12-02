import os
import google.generativeai as genai
import textwrap

from content import API_KEY

from IPython.display import Markdown

class FlashModel:

    def __init__(self):
        os.environ["GOOGLE_API_KEY"]=API_KEY
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def predict(self,text):
        responce = self.model.generate_content(text)
        res = responce.text
    
        return res
    

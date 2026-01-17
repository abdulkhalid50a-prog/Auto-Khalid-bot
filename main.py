EMAIL = "abdulkhalid50a@gmail.com"
BLOG_ID = "7285063762246613773"
import os
import smtplib
import time
from email.mime.text import MIMEText
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
B_EMAIL = os.getenv("B_EMAIL")
M_EMAIL = os.getenv("M_EMAIL")
A_PASS = os.getenv("A_PASS")

llm = ChatGroq(model="llama-3.1-8b-instant")
search = DuckDuckGoSearchRun()

topics = [
    "Latest India news updates", 
    "Technology news 2026 India", 
    "Cricket scores India match", 
    "Bollywood movie news today"
]

def post_news(query):
    try:
        data = search.run(query)
        res = llm.invoke(f"Write a professional Hindi news post. Title on line 1. Data: {data}")
        lines = res.content.split('\n')
        title = lines[0].replace('**', '').replace('#', '').strip()
        body = "<br>".join(lines[1:])
        
        img_keyword = query.split()[0]
        img_url = f"https://loremflickr.com/800/500/{img_keyword},news"
        
        html = f"""
        <div style="font-family:sans-serif; border:1px solid #ddd; padding:15px; border-radius:10px;">
            <img src="{img_url}" width="100%" style="border-radius:10px;">
            <h1 style="color:#e74c3c;">{title}</h1>
            <div style

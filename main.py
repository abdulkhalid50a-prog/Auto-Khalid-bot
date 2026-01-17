EMAIL = "abdulkhalid50a@gmail.com"
BLOG_ID = "7285063762246613773"

import os
import smtplib
import time
from email.mime.text import MIMEText
from langchain_groq import ChatGroq
from duckduckgo_search import DDGS

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
A_PASS = os.getenv("A_PASS")
M_EMAIL = os.getenv("M_EMAIL")
B_EMAIL = os.getenv("B_EMAIL")

llm = ChatGroq(model="llama-3.1-8b-instant")

def post_news(query):
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=1)]
            data = results[0]['body'] if results else "No news found"
            
        res = llm.invoke(f"Write a professional Hindi news post. Title on line 1. Data: {data}")
        lines = res.content.split('\n')
        title = lines[0].replace('*', '').replace('#', '').strip()
        body = "<br>".join(lines[1:])
        
        img_keyword = query.split()[0]
        img_url = f"https://loremflickr.com/800/500/{img_keyword},news"
        
        html = f"""
        <div style="font-family:sans-serif; border:1px solid #ddd; padding:15px; border-radius:10px;">
            <img src="{img_url}" width="100%" style="border-radius:10px;">
            <h1 style="color:#e74c3c;">{title}</h1>
            <div style="font-size:18px; line-height:1.6;">{body}</div>
            <p style="color:gray; font-size:12px;">Auto-posted by Khalid AI Bot</p>
        </div>
        """
        
        msg = MIMEText(html, 'html')
        msg['Subject'] = title
        msg['From'] = M_EMAIL
        msg['To'] = B_EMAIL
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(M_EMAIL, A_PASS)
            server.sendmail(M_EMAIL, B_EMAIL, msg.as_string())
        print(f"Success: {title}")
    except Exception as e:
        print(f"Error: {e}")

topics = ["Latest India news updates", "Entertainment news India"]

for t in topics:
    post_news(t)
    time.sleep(30)

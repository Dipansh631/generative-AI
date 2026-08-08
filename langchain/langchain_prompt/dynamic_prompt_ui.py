import re
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

def extract_clean_text(content) -> str:
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict):
                if 'text' in item:
                    parts.append(extract_clean_text(item['text']))
                elif 'type' in item and item['type'] == 'text':
                    parts.append(extract_clean_text(item.get('text', '')))
            elif isinstance(item, str):
                parts.append(extract_clean_text(item))
        return "".join(parts)
    
    if not isinstance(content, str):
        content = str(content)
        
    text_stripped = content.strip()
    if text_stripped.startswith('[') and '"extras"' in text_stripped:
        try:
            start_idx = text_stripped.find('"text":"')
            if start_idx != -1:
                start_idx += 8
                end_match = re.search(r'"\n\s*"extras"', text_stripped[start_idx:])
                if end_match:
                    end_idx = start_idx + end_match.start()
                    raw_content = text_stripped[start_idx:end_idx]
                    try:
                        return json.loads(f'"{raw_content}"')
                    except Exception:
                        decoded = raw_content.replace('\\n', '\n')
                        decoded = decoded.replace('\\"', '"')
                        decoded = decoded.replace('\\\\', '\\')
                        return decoded
        except Exception:
            pass
    return content

st.header('Research Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt(r"d:\dowl\projects\langchain\template.json")
if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
        })
    clean_content = extract_clean_text(result.content)
    st.write(clean_content)
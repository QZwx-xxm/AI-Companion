import streamlit as st
import os
from openai import OpenAI

#设置页面配置
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🐰",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题“AI智能伴侣”
st.title("AI智能伴侣")

#logo
st.logo("resources/微信图片_20250912010700.png")

#系统提示词
system_prompt = "你是一个非常可爱的AI助力，你的名字叫小甜甜，请使用温柔可爱的语气回答用户问题"

#初始化聊天
if "messages" not in st.session_state:
    st.session_state.messages = []

#展示聊天记录
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("ai").write(message["content"])

# 创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是DeepSeek的API_KEY的值）
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

#聊天信息的输入框
prompt = st.chat_input("请输入你的问题：")
if prompt:#字符串会自动转化为布尔值，如果字符串为空，则为False
    st.chat_message("user").write(prompt)
    print("---------->调用AI大模型，提示词：",prompt)
    #添加用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system",
             "content": system_prompt},
            {"role": "user", "content":prompt},
        ],
        stream=False
    )

    # 输出大模型的回复
    print("<---------------- 大模型返回的结果：",response.choices[0].message.content)
    st.chat_message("ai").write(response.choices[0].message.content)
    #添加大模型返回的回复
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
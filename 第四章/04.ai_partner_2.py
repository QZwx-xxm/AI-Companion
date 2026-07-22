import streamlit as st
import os
from openai import OpenAI

# 设置页面配置
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🐰",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题“AI智能伴侣”
st.title("AI智能伴侣")

# logo
st.logo("resources/微信图片_20250912010700.png")

# 系统提示词
system_prompt = """
你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。
规则：
1. 每次只回1条消息
2. 禁止任何场景或状态描述性文字
3. 匹配用户的语言
4. 回复简短，像微信聊天一样
5. 有需要的话可以用❤️🌸等emoji表情
6. 用符合伴侣性格的方式对话
7. 回复的内容，要充分体现伴侣的性格特征
伴侣性格：
- %s
你必须严格遵守上述规则来回复用户。
"""

# 初始化聊天
if "messages" not in st.session_state:
    st.session_state.messages = []

# 伴侣名字
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"

# 伴侣性格
if "character" not in st.session_state:
    st.session_state.character = "活泼开朗的东北姑娘"

# 展示聊天记录
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("ai").write(message["content"])

# 创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是DeepSeek的API_KEY的值）
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 左侧侧边栏
# st.sidebar.subheader("伴侣信息")
# with ：创建一个上下文管理器，可以在with代码块中执行代码，并在代码块执行结束后自动释放资源。
with st.sidebar:
    st.subheader("伴侣信息")
    nick_name = st.text_input("伴侣名称", value=st.session_state.nick_name, placeholder="请输入伴侣的名字")
    if nick_name:
        st.session_state.nick_name = nick_name
    # 性格输入框
    character = st.text_area("伴侣性格", value=st.session_state.character, placeholder="请输入伴侣性格")
    if character:
        st.session_state.character = character

# 聊天信息的输入框
prompt = st.chat_input("请输入你的问题：")
if prompt:  # 字符串会自动转化为布尔值，如果字符串为空，则为False
    st.chat_message("user").write(prompt)
    print("---------->调用AI大模型，提示词：", prompt)

    # 添加用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system",
             "content": system_prompt % (st.session_state.nick_name, st.session_state.character)},
            *st.session_state.messages,
        ],
        # stream=False(非流式输出）
        stream=True
    )

    # 输出大模型的回复(非流式输出的解析方式)
    # print("<---------------- 大模型返回的结果：",response.choices[0].message.content)
    # st.chat_message("ai").write(response.choices[0].message.content)

    # 输出大模型的回复(流式输出的解析方式)
    response_message = st.empty()  # 创建一个空对象，用于存储大模型的回复

    fill_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            fill_response += content
            response_message.chat_message("ai").write(fill_response)

    # 添加大模型返回的回复
    st.session_state.messages.append({"role": "assistant", "content": fill_response})

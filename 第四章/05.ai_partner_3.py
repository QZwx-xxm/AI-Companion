import streamlit as st
import os
from openai import OpenAI
from datetime import *
import json

# 设置页面配置
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🐰",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)


# 定义函数保存会话信息文件
def save_session(session_id):
    # 保存当前会话信息
    if st.session_state.session_id:
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "character": st.session_state.character,
            "session_id": st.session_state.session_id,
            "messages": st.session_state.messages
        }
        # 如果session目录不催在，则创建
        if not os.path.exists("session"):
            os.mkdir("session")
        # 保存会话信息
        with open(f"session/{st.session_state.session_id}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)


# 生产会话标识
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# 加载所有会话信息
def load_session():
    session_list = []
    # 加载session目录下的所有会话信息
    if os.path.exists("session"):
        file_list = os.listdir("session")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    session_list.sort(reverse=True)
    return session_list


# 加载指定会话信息
def load_sessions(session_id):
    try:
        if os.path.exists(f"session/{session_id}.json"):
            with open(f"session/{session_id}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
            st.session_state.nick_name = session_data["nick_name"]
            st.session_state.character = session_data["character"]
            st.session_state.session_id = session_data["session_id"]
            st.session_state.messages = session_data["messages"]
    except Exception as e:
        st.error("加载会话失败！")


# 删除会话信息函数
def delete_session(session_id):
    try:
        if os.path.exists(f"session/{session_id}.json"):
            os.remove(f"session/{session_id}.json")  # 删除文件
            # 如果删除的是当前会话，则需要更新消息列表
            if session_id == st.session_state.session_id:
                st.session_state.messages = []
                st.session_state.session_id = generate_session_name()
    except Exception:
        st.error("删除会话失败！")


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

# 会话标识
if "session_id" not in st.session_state:
    st.session_state.session_id = generate_session_name()

# 展示聊天记录
st.subheader(f"会话名称:{st.session_state.session_id}")
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
    # 会话信息
    st.subheader("AI控制面板")

    # 增加按钮
    if st.button("新建会话", width="stretch", icon="✏️"):
        # 保存当前会话信息
        save_session(st.session_state.session_id)

        # 创建会话信息文件
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.session_id = generate_session_name()
            save_session(st.session_state.session_id)
            st.rerun()  # 重新运行当前页面

    # 会话历史
    st.text("会话历史")
    session_list = load_session()
    for session in session_list:
        col1, col2 = st.columns([4, 1])
        with col1:
            # 加载会话信息
            # 三元运算符：值1 if 条件 else 值2 ：表示如果条件表达式为真，则返回表达式1，否则返回表达式2。
            if st.button(session, width="stretch", icon="📋", key=f"load_{session}",
                         type="primary" if session == st.session_state.session_id else "secondary"):
                load_sessions(session)
                st.rerun()
        with col2:
            # 删除会话信息
            if st.button("", width="stretch", icon="❌", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()
        # st.button(session, width="stretch", icon="📋")

    # 分割线
    st.divider()

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

    # 保存当前会话信息
    save_session(st.session_state.session_id)

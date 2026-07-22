import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

# 设置页面配置
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🐰",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)


# 保存会话函数
def save_session():
    if st.session_state.session_id:
        session_deta = {
            "ai_name": st.session_state.ai_name,
            "ai_sex": st.session_state.ai_sex,
            "session_id": st.session_state.session_id,
            "messages": st.session_state.messages
        }

        # 判断是否存在文件目录，要将文件存放在文件目录下，如果没有文件目录，则创建一个文件目录
        if not os.path.exists("session"):
            os.mkdir("session")

        with open(f"session/{st.session_state.session_id}.json", "w", encoding="utf-8") as f:
            json.dump(session_deta, f, ensure_ascii=False, indent=2)


# 所有的文件名，不带.json
def load_sessions():
    session_list = []
    if os.path.exists("session"):
        feli_list = os.listdir("session")
        for feliname in feli_list:
            if feliname.endswith(".json"):
                session_list.append(feliname[:-5])
    session_list.sort(reverse=True)
    return session_list


# 加载指定会话
def load_session(session_id):
    try:
        if os.path.exists(f"session/{session_id}.json"):
            with open(f"session/{session_id}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
            st.session_state.ai_name = session_data["ai_name"]
            st.session_state.ai_sex = session_data["ai_sex"]
            st.session_state.session_id = session_data["session_id"]
            st.session_state.messages = session_data["messages"]
    except Exception:
        st.error("加载会话失败")


def delete_session(session_id):
    try:
        if os.path.exists(f"session/{session_id}.json"):
            os.remove(f"session/{session_id}.json")
            # 如果删除的会话名字和现在正在运行的会话名字一样则新建一个会话，否则不管
            if session_id == st.session_state.session_id:
                st.session_state.messages = []
                st.session_state.session_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                save_session()
                st.rerun()
    except Exception:
        st.error("删除会话失败")


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

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 设置标题
st.title("AI智能伴侣")

# 建立一个空列表，用于存储聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 设置AI名字的默认值，把他放入在列表中
if "ai_name" not in st.session_state:
    st.session_state.ai_name = "小甜甜"

# 设置AI性格的默认值，把他放入在列表中
if "ai_sex" not in st.session_state:
    st.session_state.ai_sex = "性格爽朗的东北姑娘"

# 设置时间作为文件名字(设置默认值)，把他放入在列表中
if "session_id" not in st.session_state:
    st.session_state.session_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 时间显示
st.write(f"会话名称：{st.session_state.session_id}")

# 展示聊天记录
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 侧边栏
with st.sidebar:
    st.subheader("AI控制面板")
    # 新建对话按钮
    if st.button("新建对话", width="stretch", icon="✏️"):
        # 保存当前会话
        save_session()

        # 创建一个新的对话
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.session_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            save_session()
            st.rerun()

    st.write("历史对话")
    session_list = load_sessions()
    for session in session_list:
        col1, col2 = st.columns([4, 1])
        with col1:
            if st.button(session, width="stretch", icon="📋", key=f"lard_{session}",type="primary" if session==st.session_state.session_id else "secondary"):
                load_session(session)
                st.rerun()

        with col2:
            if st.button("", width="stretch", icon="❌", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    # file_list=[]
    # session_list = os.listdir("session")
    # for session in session_list:
    #     if session.endswith(".json"):
    #         file_list.append(session[:-5])
    #         col1, col2 = st.columns([4, 1])
    #         with col1:
    #             if st.button(st.session_state.session_id, width="stretch", icon="📋",key=f"lard_{session}"):
    #                 try:
    #                     if os.path.exists(f"session/{st.session_state.session_id}.json"):
    #                         with open(f"session/{st.session_state.session_id}.json", "r", encoding="utf-8") as f:
    #                             session_data = json.load(f)
    #                         st.session_state.ai_name = session_data["ai_name"]
    #                         st.session_state.ai_sex = session_data["ai_sex"]
    #                         st.session_state.session_id = session_data["session_id"]
    #                         st.session_state.messages = session_data["messages"]
    #                 except Exception as e:
    #                     print("加载会话失败")
    #                 st.rerun()
    #
    #         with col2:
    #             if st.button("", width="stretch", icon="❌", key=f"delter_{session}"):
    #                 try:
    #                     if os.path.exists(f"session/{st.session_state.session_id}.json"):
    #                         os.remove(f"session/{st.session_state.session_id}.json")
    #                 except Exception as e:
    #                     print("删除会话失败")

    #分割线
    st.divider()

    st.subheader("伴侣信息")
    ai_name = st.text_input("名字", value=st.session_state.ai_name, placeholder="请输入伴侣的名字")
    if ai_name:
        st.session_state.ai_name = ai_name
    ai_sex = st.text_area("性格", value=st.session_state.ai_sex, placeholder="请输入伴侣的性格")
    if ai_sex:
        st.session_state.ai_sex = ai_sex

# 设置输入框
assume = st.chat_input("请输入您的问题...")

if assume:
    st.chat_message("user").write(assume)
    # 在列表中添加用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": assume})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt % (ai_name, ai_sex)},
            *st.session_state.messages
        ],
        stream=True
    )

    # 构建一个空的空间，用于存储大模型返回的回复
    response_message = st.empty()

    total_content = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            total_content += chunk.choices[0].delta.content
            response_message.chat_message("ai").write(total_content)

    # 添加大模型返回的回复
    st.session_state.messages.append({"role": "assistant", "content": total_content})

    #保存回答信息
    save_session()
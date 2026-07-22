import streamlit as st

# 大标题
st.title("Streamlit入门演示")
st.header("一级标题")
st.subheader("二级标题")

# 段落文字
st.write("请大家注意各方面安全，合理规划时间，度过一个平安、健康、快乐的假期")
st.write("暑假放假及开学时间如下：")
st.write("2026年7月20日（星期一）至8月28日（星期五）放暑假，共6周；")
st.write("2026年8月29日（星期六）、8月30日（星期日）学生返校报到，8月31日（星期一）正式上班上课。")

# 图片
st.image("./resources/微信图片_20251127215855_26_1.jpg")
# 音频
st.audio("resources/录音.m4a")
# 视频
st.video("resources/4d84bd1403ae037d41f53c5d08f8f8f0.mp4")
# logo
st.logo("resources/微信图片_20250912010700.png")
# 表格
student_data = {
    "姓名": ["网络", "张宁", "张佳瑶"],
    "学号": ["123", "456", "789"]
}
st.table(student_data)

# 输入框
word = st.text_input("请输入姓名：")
st.write(f"您输入的姓名为：{word}")

# 密码输入框
password = st.text_input("请输入密码：",type="password")
st.write(f"您输入的密码为：{password}")

#单选按钮
sex=st.radio("请输入您的性别：",["男","女","其他"])
st.write(f"您输入的性别为：{sex}")
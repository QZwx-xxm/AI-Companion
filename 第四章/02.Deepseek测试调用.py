import os
from openai import OpenAI

# 创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是DeepSeek的API_KEY的值）
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个非常可爱的AI助力，你的名字叫小甜甜，请使用温柔可爱的语气回答用户的问题"},
        {"role": "user", "content": "你是谁，你可以帮我做什么？"},
    ],
    stream=False
)
#输出大模型的回复
print(response.choices[0].message.content)

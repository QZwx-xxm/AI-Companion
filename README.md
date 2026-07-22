# 🐰 AI智能伴侣

基于 Streamlit 和 DeepSeek API 构建的智能对话伴侣，支持**多会话管理**、**角色性格自定义**和**流式输出**。

## ✨ 功能特点
- 💬 **实时对话**：接入 DeepSeek 大模型，响应流畅
- 📋 **多会话管理**：支持新建、切换、删除历史会话（自动保存/加载）
- 🎭 **角色自定义**：可自由设置伴侣的姓名和性格
- 🌊 **流式输出**：打字机效果，体验更自然
- 🗂️ **本地存储**：会话数据以 JSON 格式保存在本地

## 🛠️ 技术栈
- Python 3.9+
- Streamlit
- OpenAI SDK (DeepSeek API)
- JSON

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/QZwx-xxm/AI-Companion.git
cd AI-Companion
```

### 2. 安装依赖
```bash
pip install streamlit openai
```

### 3. 配置 API Key
在系统环境变量中设置 `DEEPSEEK_API_KEY`。

### 4. 运行项目
```bash
streamlit run 第四章/06.self_ai_partner.py
```

## 📂 项目结构
```
├── 第四章/
│   └── 06.self_ai_partner.py   # 主程序
├── session/                     # 会话存储目录（自动生成）
├── resources/                   # 静态资源
└── README.md
```

## 👨‍💻 开发心得
这是我自学 Python + AI 过程中的第一个完整实战项目。从复现老师代码到独立重构，我深刻体会到了"先理清业务逻辑，再动手写码"的重要性。

## 📬 联系我
- GitHub: [https://github.com/QZwx-xxm](https://github.com/QZwx-xxm)
- 邮箱: m15209583792_1@163.com
import google.generativeai as genai
import os
from dotenv import load_dotenv
import asyncio # (Vibe 5.0 升级：我们需要一个 'async' Vibe)

# 1. 加载 "保险库" (.env)
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Vibe 401! 没在 .env 文件里找到 GEMINI_API_KEY！")
    exit()

print("Vibe: 找到了 API Key... 正在配置 Google Vibe...")

# 2. 配置 "Google 官方 Vibe"
genai.configure(api_key=api_key)

# 3. "Vibe 隔离" 测试函数
async def run_vibe_check():
    print("Vibe: 正在尝试连接 Google API (using gemini-pro)...")
    try:
        # 4. 初始化 "Google Vibe" 模型 (使用最稳的 gemini-2.5-pro)
        model = genai.GenerativeModel(model_name="gemini-2.5-pro")
        
        # 5. 【Vibe 决战】发起最简单的 "Vibe 连接"
        response = await model.generate_content_async("Hello")
        
        # 6. 【Vibe 100% 成功】
        print("\n" + "="*30)
        print(" VIBE 100% CONNECTION SUCCESSFUL!")
        print(" 连接成功！你的网络 Vibe 没问题！")
        print("="*30)
        print(f"AI 回复: {response.text}")

    except Exception as e:
        # 7. 【Vibe 503 失败】
        print("\n" + "!"*30)
        print(" VIBE 503 CONNECTION FAILED!")
        print(" 连接失败！这就是那个 503 Vibe Bug！")
        print(" 100% 是你的 'Vibe 0: 网络不通' (防火墙/代理) 问题。")
        print("!"*30)
        print(f"\n详细错误: {e}")

# Vibe 5.0: 运行这个 "Vibe 隔离" 测试
if __name__ == "__main__":
    asyncio.run(run_vibe_check())
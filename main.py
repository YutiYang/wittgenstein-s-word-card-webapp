from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI, RateLimitError, APIConnectionError, AuthenticationError
import os
from dotenv import load_dotenv
import json

# --- Vibe 启动 (不变) ---
load_dotenv()
app = FastAPI()

# --- Vibe 6.5: CORS "Vibe 门禁卡" 激活 ---
# Vibe 定义 "Vibe 信任" 的来源 (Origins)

origins = [
    "https://wittgenstein-s-word-card-webapp.vercel.app", # Vibe 授权: 你的 Vercel Vibe 域名
    "http://127.0.0.1:5500", # Vibe 授权: Day 1 的 Live Server (Vibe 调试用)
    "http://localhost:5500",  # Vibe 授权: Day 1 的 Live Server (Vibe 调试用)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Vibe 只允许 "Vibe 信任" 的人 Vibe 访问
    allow_credentials=True,
    allow_methods=["*"],    # Vibe 允许 "Vibe 任何" 方法 (GET, POST etc.)
    allow_headers=["*"],    # Vibe 允许 "Vibe 任何" 头部
)

# --- 1. 定义 "JSON 灵魂" (不变) ---
class GameBoard(BaseModel):
    context: str
    sentence: str

class WordCardResponse(BaseModel):
    word: str
    core_game: str
    language_games: list[GameBoard]
    collocations: list[str]
    mnemonic_tip: str

class CardRequest(BaseModel):
    word: str
    model: str # (这是 "Vibe 友好名", e.g., "gemini-pro")

# --- 2. 注入 "AI 灵魂" (不变) ---
SYSTEM_PROMPT = """
You are a "Language Game Designer" steeped in Wittgenstein's philosophy. 
Your task is NOT to define a word, but to provide a clear, fun "game manual" (in JSON format) guiding users on how to "use" the word in different contexts.

You must generate all content (keys and values) in English, based on the user's word.

You MUST and ONLY return a single, valid JSON object that strictly adheres to this Pydantic schema:

{
  "word": "The target word",
  "core_game": "This is the 'Core Game'. A single sentence explaining the 'language game' or 'contextual scene' where this word is a key card. E.g., for 'Ephemeral', the core game is 'Capturing and lamenting fleeting beauty'.",
  "language_games": [
    {
      "context": "Board A (e.g., Speculative Scene)",
      "sentence": "An example sentence for this abstract or formal context."
    },
    {
      "context": "Board B (e.g., Daily Life Scene)",
      "sentence": "An example sentence for this everyday or informal context."
    }
  ],
  "collocations": [
    "A very common 2-3 word phrase using the word.",
    "Another common 2-3 word phrase."
  ],
  "mnemonic_tip": "A clever, surprising 'Mnemonic Tip' to lock in the word's 'play style'. This is the 'Winning Move'."
}

Do not include any other text, markdown, apologies, or explanations outside of this single JSON object.
"""

# --- 3. 【Vibe 6.0: The "Vibe Model Map"】---
# 你的 Vibe 核心需求: "开发者可以简单快速的修改"
VIBE_MODEL_MAP = {
    # Day 1 "gemini-flash" 映射
    "gemini": {
        "model_name": "gemini-2.5-pro", # 你的 Vibe 需求: Flash 不好用，映射到 Pro
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
        "api_key": os.getenv("GEMINI_API_KEY")
    },
    # Vibe 6.0 新增 "deepseek" 映射
    "deepseek": {
        "model_name": "gemini-2.5-flash", # 你的 Vibe 需求
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/", # (DeepSeek 的标准 Vibe URL)
        "api_key": os.getenv("GEMINI_API_KEY")
    }
}

# --- 4. 升级 "API 接口" (【Vibe 6.0 Model Map 版】) ---
@app.post("/generate-card", response_model=WordCardResponse)
async def generate_card(request: CardRequest):
    print(f"--- 接收到制卡请求 (Vibe 6.0) ---")
    print(f"前端 Vibe 名: {request.model}, 单词: {request.word}")

    # 1. 【Vibe 6.0 核心】执行 Vibe 映射
    frontend_model_name = request.model
    model_config = VIBE_MODEL_MAP.get(frontend_model_name)

    # Vibe Check: 前端传来的 Vibe 名，我们在 Map 里认识吗？
    if not model_config:
        print(f"--- VIBE 404: 模型未找到 ---")
        raise HTTPException(status_code=404, detail=f"VIBE 404: 未知的 'Vibe 友好名': {frontend_model_name}")

    # 2. Vibe Check: 这个 Vibe 模型的 API Key "保险库" 里有吗？
    backend_api_key = model_config.get("api_key")
    if not backend_api_key:
        print(f"--- VIBE 500: API Key 未配置 ---")
        raise HTTPException(status_code=500, detail=f"VIBE 500: 后端 .env 未配置 {frontend_model_name} 对应的 API Key")

    # 3. 【Vibe 6.0 核心】动态配置 "OpenAI Vibe" 客户端
    # (我们不能再用 "Vibe 3.0" 的全局 client 了)
    try:
        client = OpenAI(
            api_key=backend_api_key,
            base_url=model_config.get("base_url")
        )
        
        backend_model_name = model_config.get("model_name")
        print(f"Vibe 映射成功: 正在使用 {backend_model_name} @ {model_config.get('base_url')}")

        # 4. 调用 AI (Vibe 3.0 逻辑)
        response = client.chat.completions.create(
            model=backend_model_name, # 使用 "Vibe 真实名"
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": request.word}
            ]
        )
        
        # 5. 提取 AI 响应 (Vibe 3.0 逻辑)
        ai_response_text = response.choices[0].message.content
        print("--- AI 原始响应 (字符串) ---")
        print(ai_response_text)

        # 6. 【Vibe 2.0 清理代码】(不变, Vibe 1.0 的 Bug 修复)
        json_start = ai_response_text.find('{')
        json_end = ai_response_text.rfind('}') + 1
        
        if json_start == -1 or json_end == 0:
            raise ValueError("AI Vibe Check: 响应中未找到有效的 JSON。")

        clean_json_string = ai_response_text[json_start:json_end]
        print("--- 清理后的 JSON 字符串 ---")
        print(clean_json_string)

        # 7. 解析 "纯净" JSON (不变)
        ai_json = json.loads(clean_json_string)
        
        # 8. 返回工整的 JSON (不变)
        return ai_json

    # --- Vibe 3.0 智能诊断 (不变) ---
    except RateLimitError as e:
        print(f"--- VIBE 诊断: 速率限制 (RPM=2?) ---")
        print(e)
        raise HTTPException(status_code=429, detail=f"VIBE 429: Too Many Requests. (RPM 限制了，请 Vibe 冷却 30 秒！)")
    
    except APIConnectionError as e:
        print(f"--- VIBE 诊断: 真实连接错误 ---")
        print(e)
        raise HTTPException(status_code=503, detail=f"VIBE 503: API Connection Error. (100% 是 Vibe 0: 网络不通 / 防火墙)")

    except AuthenticationError as e:
        print(f"--- VIBE 诊断: API Key 错误 ---")
        print(e)
        raise HTTPException(status_code=401, detail="VIBE 401: Authentication Error. 你的 API Key 是错的。")

    except Exception as e:
        print(f"--- VIBE 诊断: JSON 解析或其他 Vibe 错误 ---")
        print(e)
        raise HTTPException(status_code=500, detail=f"AI Vibe Check Failed: {str(e)}")

# Day 4 的 "Vibe" 检查路径 (不变)
@app.get("/")
async def read_root():
    return {"Vibe": "后端服务器已启动，AI 模块 Vibe 6.0 (Model Map) 已加载！"}
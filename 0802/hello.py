"""
簡單的 Gemini 互動式對話程式
使用方式：uv run 0802/hello.py
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
# 載入 .env 檔案中的環境變數
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise EnvironmentError(
        "找不到 GEMINI_API_KEY，請在專案根目錄建立 .env 檔案並設定該變數。\n"
        "範例：GEMINI_API_KEY=你的金鑰\n"
        "取得金鑰：https://aistudio.google.com/app/apikey"
    )

client = genai.Client(api_key=API_KEY)
MODEL = "gemini-2.0-flash"

# 保存對話歷史
history: list[types.Content] = []

print("=== Gemini 對話模式 ===")
print(f"模型：{MODEL}")
print("輸入 'exit' 或 'quit' 結束對話\n")

while True:
    try:
        user_input = input("你：").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n再見！")
        break

    if not user_input:
        continue

    if user_input.lower() in ("exit", "quit"):
        print("再見！")
        break

    # 加入使用者訊息
    history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))

    response = client.models.generate_content(
        model=MODEL,
        contents=history,
    )

    reply = response.text
    print(f"Gemini：{reply}\n")

    # 加入模型回應，保持對話上下文
    history.append(types.Content(role="model", parts=[types.Part(text=reply)]))

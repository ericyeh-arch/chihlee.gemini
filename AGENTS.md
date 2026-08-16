# AGENTS.md

這是使用 uv 虛擬環境（Python 3.12，見 `.python-version`）。所有依賴與執行都用 `uv`，勿用 pip/venv。
不管輸入英文或中文，全部以繁體中文回覆。

## 專案結構
- 非套件：沒有 src 布局，`.py` 腳本與 Jupyter notebook 直接在專案根目錄執行，例如 `uv run 0802/hello.py`。
- 練習按日期分目錄：`0802/`、`0809/`、`0816/`（MMDD = 月日）。新增練習應放入對應日期資料夾。
- 根目錄的 `practice2.ipynb` 是 0816 的複本；同名檔可能在 `0816/`（注意 `0816/practice2 .ipynb` 檔名含空格）。

## 環境變數
- 需要 `GEMINI_API_KEY`，由 python-dotenv 從根目錄 `.env` 載入。`.env` 被 gitignore，範本在 `.env.example`。
- 腳本沒設金鑰會直接報錯並提示建立 `.env`。

## 依賴
- `pyproject.toml` 只有 google-genai、ipykernel、python-dotenv。
- `0816/practice4.py` 使用了 **gradio，但未列為依賴**；要跑它先 `uv add gradio`。
- 新增第三方套件一律用 `uv add <套件>`。

## 程式碼慣例
- 每個檔案用到的 Gemini 模型名稱不同：`0802/hello.py` 用 `gemini-2.0-flash`，0809/0816 用 `gemini-3.5-flash`（可能不存在於現行 API）。改寫時沿用該檔案原有的模型名稱，不要自作主張統一。
- 腳本語系為繁體中文（含註解、docstring、提示訊息）。

## 驗證
- 沒有測試、lint、format、typecheck 設定。驗證方式就是實際執行腳本或 cell，確認無語法錯誤且能讀取 `.env`。

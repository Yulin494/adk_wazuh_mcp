# adk_wazuh_mcp

先進入虛擬環境
"""
# Create
python -m venv .venv
# Activate (each new terminal)
# macOS/Linux: source .venv/bin/activate
# Windows CMD: .venv\Scripts\activate.bat
# Windows PowerShell: .venv\Scripts\Activate.ps1
"""


下載套件
"""
pip install google-adk
"""

然後需要建立一個 wazuh 的.env，並且把 agent.py的路徑改成你設定的路徑
wazuh .env的內容在hackmd內
docker 要記得開啟

也需要在multi_tool_agent建立一個.env檔案

.env如下
"""
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YourGoogleApiKey
"""

啟動server
"""
adk api_server .  
"""

啟動後，需要先建立一個sessionID

```bash
# Method: POST
# Path: /apps/{app_name}/users/{user_id}/sessions/{session_id}
# request body
# {
#   "state": {
#     "key1": "value1",
#     "key2": 42
#   }
# }

curl -X POST http://localhost:8000/apps/multi_tool_agent/users/u_123/sessions/s_123 \
  -H "Content-Type: application/json" \
  -d '{"state": {"key1": "value1", "key2": 42}}'
```

run 主要的詢問

```bash
# Method: POST
# Path: /run
# Request Body


# {
#   "app_name": "my_sample_agent",
#   "user_id": "u_123",
#   "session_id": "s_abc",
#   "new_message": {
#     "role": "user",
#     "parts": [
#       { "text": "What is the capital of France?" }
#     ]
#   }
# }

curl -X POST http://localhost:8000/run \
-H "Content-Type: application/json" \
-d '{
    "app_name": "multi_tool_agent",
    "user_id": "u_123",
    "session_id": "s_123",
    "new_message": {
        "role": "user",
        "parts": [{
            "text": "請給我最近五筆wazuh警報"                
        }]
    }
}'
```



詳細資料
https://google.github.io/adk-docs/get-started/testing/#local-testing

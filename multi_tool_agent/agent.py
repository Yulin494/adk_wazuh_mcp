import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

wazuh_toolset = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='docker',
            args=[
                "run", "--rm", "-i",
                "--env-file", "/Users/imac/WazuhMcp/.env", # 請將此路徑替換為你的 WazuhMcp .env 檔案路徑
                "ghcr.io/gbrigandi/mcp-server-wazuh:latest"
            ],
        ),
    ),
)

cortex_toolset = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='/Users/imac/.cargo/bin/mcp-server-cortex',  # 請將此路徑替換為你的 mcp-server-cortex 可執行檔路徑
            args=[],
            env={
                "CORTEX_ENDPOINT": "Your Cortex Endpoint",
                "CORTEX_API_KEY": "Your Cortex API Key",
                "RUST_LOG": "info"
            },
        ),
    ),
)

root_agent = LlmAgent(
    model='gemini-2.5-flash', 
    name='wazuh_agent', 
    instruction=(
        "你是一個 Wazuh 結合 cortex 資安助理。你的任務是使用提供的工具來回答關於 Wazuh 平台的查詢並且使用cortex 分析儀分析可疑的ip或url。"
        "如果使用者說查詢最近幾筆的話，就limit在5筆以內。"
        "請根據使用者的問題，選擇最合適的工具來回覆準確的資訊，並且把得到的資訊彙整起來給使用者。"
        "只把標題放大，並改成紅色字"
    ),
    tools=[
        wazuh_toolset,
        cortex_toolset
    ],
)
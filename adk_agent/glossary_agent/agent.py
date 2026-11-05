"""第3回: Google ADK で作る学習支援エージェント。

使い方（リポジトリのルートで実行）:
    PYTHONPATH=. uv run --with google-adk adk run adk_agent/glossary_agent
    # 起動後、質問を入力する。終了するときは exit と入力する。

Pydantic AI 版と同じ指示・ツールを使い、ADK でエージェントを組み立てる。
"""

from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from app import tools
from app.agent import INSTRUCTIONS

root_agent = Agent(
    model="gemini-3.5-flash-lite",
    name="glossary_agent",
    instruction=INSTRUCTIONS,
    tools=[
        tools.search_glossary,
        tools.get_lecture_summary,
        tools.make_quiz,
        FunctionTool(
            func=tools.save_learning_log,
            require_confirmation=True,
            )
        ],
    )

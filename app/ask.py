"""第1回: 会話履歴を保ちながらLLMに質問するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 最初の発言を省略すると、既定の発言を送る

ツールは使わず、質問と回答の履歴を次の応答に渡す。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse

from google import genai
from google.genai import errors
from google.genai import types

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"
INITIAL_MESSAGE = "私の好きな色は青です。好きな果物はりんごです。覚えておいてください。"


def ask(
    client: genai.Client,
    question: str,
    history: list[types.Content],
) -> str:
    history.append(types.Content(role="user", parts=[types.Part(text=question)]))
    response = client.models.generate_content(model=MODEL, contents=history)


    usage = response.usage_metadata
    print(
        f"[トークン数] 入力（会話履歴を含む）: {usage.prompt_token_count} / "
        f"出力（今回の回答）: {usage.candidates_token_count}"
    )

    answer = response.text or ""
    history.append(types.Content(role="model", parts=[types.Part(text=answer)]))
    return answer


def main() -> None:
    parser = argparse.ArgumentParser(description="会話できるLLMに質問する")
    parser.add_argument("question", nargs="?", default=INITIAL_MESSAGE)
    args = parser.parse_args()

    print(f"[model] {MODEL}")
    print("終了するには exit または quit と入力してください。")
    history: list[types.Content] = []
    question = args.question
    try:
        client = genai.Client(api_key=get_api_key())
        while question.lower() not in {"exit", "quit"}:
            if question:
                print(f"[あなた] {question}\n")
                print(ask(client, question, history))
            question = input("\次の入力: ").strip()
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()

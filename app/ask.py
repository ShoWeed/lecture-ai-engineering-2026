"""第1回: 素のLLMに1回だけ質問するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする

ツールも会話履歴も持たない「素の」呼び出し。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"

def main() -> None:
    parser = argparse.ArgumentParser(description="素のLLMに質問する（チャット対応）")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    print(f"[model] {MODEL}")

    client = genai.Client(api_key=get_api_key())
    chat = client.chats.create(model=MODEL)

    # 初回起動時
    if args.question:
        print(f"[質問] {args.question}\n")
        try:
            response = chat.send_message(args.question)
            print(f"入力トークン数: {response.usage_metadata.prompt_token_count:,}")
            print(f"出力トークン数: {response.usage_metadata.candidates_token_count:,}")
            print(response.text)
        except errors.APIError as e:
            print(api_error_message(e.code, e.message))
            raise SystemExit(1)

    # loop
    print("\n---  'exit' または 'quit' と入力 ---")
    while True:
        try:
            user_input = input("\n[質問]: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit"):
                print("終了します。")
                break

            response = chat.send_message(user_input)

            print(f"入力トークン数: {response.usage_metadata.prompt_token_count:,}")
            print(f"出力トークン数: {response.usage_metadata.candidates_token_count:,}")
            print(f"\n{response.text}")

        except errors.APIError as e:
            print(api_error_message(e.code, e.message))
        except (KeyboardInterrupt, EOFError):
            print("\n終了します。")
            break


if __name__ == "__main__":
    main()

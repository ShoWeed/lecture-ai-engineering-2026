# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
つらつらと長い問題が出てきたが、make_quizを登録した後はglossaryの内容をしっかり出力できた。
- `--trace` で見えたツール呼び出し（ツール名と引数）：
[tool call]   make_quiz({'lecture': 2})
- 1つの質問での LLM 呼び出し回数（`requests`）：
input_text_tokens=1050, input_tokens=1050, output_tokens=79, requests=2, tool_calls=1)
- 追加したツールと、docstring に書いた説明：
    """指定した回の用語から 1つを選び、
    確認問題と答えを返す。
    「第2回の確認問題を出して」のように、
    復習用の問題を求められたときに使う。
    lecture:演習の第何回かを設定する。intで1-5の範囲。
    """

## 宿題

- 取り組んだレベル：基礎 / 実装
- やったこと：
INSTRUCTIONS や docstringを変更。
 save_learning_log とrequires_approvalをつけて登録
- 結果：
INSTRUCTIONS や docstringを変更。
【変更前】
[usage] RunUsage(cost=Decimal('0.0005506'), details={'text_prompt_tokens': 727}, input_text_tokens=727, input_tokens=727, output_tokens=133, requests=2, tool_calls=1)
【変更後】
[usage] RunUsage(cost=Decimal('0.0005899'), details={'text_prompt_tokens': 833}, input_text_tokens=833, input_tokens=833, output_tokens=136, 
requests=2, tool_calls=1)

 save_learning_log とrequires_approvalをつけて登録
 →関数とagent.tool_plain(tools.save_learning_log, requires_approval=True)を登録。
- 気づき・疑問：
 INSTRUCTIONS や docstringを変更してみたが、意外と結果が変わらなく意外だった。
 性能が高いと指示が明確でなくてもできるのか？
 agent.tool_plain(tools.save_learning_log, requires_approval=True)をAIの指導のもと、登録してみたが、何も藩王がなかった。
 CLIを利用するタスクはなかったのかな。
 もっと検証したいが時間がとれないのでここまで。
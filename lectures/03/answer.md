# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：tool calling を通じて質問項目を取得して質問に回答。
- `--trace` で見えたツール呼び出し（ツール名と引数）：[search_glossary], [get_lecture_summary], [make_quiz]
- 1つの質問での LLM 呼び出し回数（`requests`）：2 回
- 追加したツールと、docstring に書いた説明：[make_quiz] / - 確認問題を求められたら make_quiz を使い、問題と答えを提示する。

## 宿題

- 取り組んだレベル：実装 & 発展
- やったこと：save_learning_log の tool を追加し学習内容を learning_log に保存、Google ADK で再実装
- 結果：学習記録の要約をの保存を CLI で利用者が内容を確認・承認し実行できるように変更
- 気づき・疑問：プロンプトを調整し。保存依頼の返答を会話内で済ませず、ツールを正しく呼び出し確認は CLI で行えるようにすることを指示に明記
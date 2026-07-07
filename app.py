import streamlit as st
import random

# ページ設定
st.set_page_config(
    page_title="キングフィッシャーズ検定",
    page_icon="🏀"
)

st.title("🏀 キングフィッシャーズ検定")

# -------------------------------
# 問題
# -------------------------------
questions = [
    {"q":"１．１試合、何Ｑ（クォーター）ある？","choices":["２Ｑ","３Ｑ","４Ｑ","６Ｑ"],"answer":"４Ｑ"},
    {"q":"２．ショットクロックは何秒？","choices":["１２秒","２４秒","３０秒","３６秒"],"answer":"２４秒"},
    {"q":"３．フリースローが１本入ったら何点？","choices":["１点","２点","３点","４点"],"answer":"１点"},
    {"q":"４．タイムアウトは何秒？※ミニバス公式ルールとして","choices":["３０秒","４５秒","６０秒","８０秒"],"answer":"６０秒"},
    {"q":"５．スローインの際、何秒以内にパスを出さなければならない？","choices":["３秒","４秒","５秒","６秒"],"answer":"５秒"},
    {"q":"６．フリースローはボールを渡されてから何秒以内にシュートを打たなければならない？","choices":["３秒","５秒","８秒","１０秒"],"answer":"５秒"},
    {"q":"７．パスを受けてから何秒以内にシュート・パス・ドリブルのいずれかを行わなければならない？","choices":["２秒","３秒","４秒","５秒"],"answer":"５秒"},
    {"q":"８．オフェンスがペイントエリア内に何秒以上、居座ってはいけない？","choices":["２秒","３秒","５秒","１０秒"],"answer":"３秒"},
    {"q":"９．１試合で同じ選手が何回ファウルしたら退場になる？","choices":["３回","４回","５回","ミニバスは退場にならない"],"answer":"５回"},
    {"q":"１０．コートに入れる人数は１チーム何人？","choices":["4人","5人","6人","7人"],"answer":"5人"},
    {"q":"１１．試合は何分間のクォーターを４回行う？","choices":["5分","6分","8分","10分"],"answer":"8分"},
{"q":"１２．試合開始は何で始まる？","choices":["フリースロー","ジャンプボール","スローイン","ドリブル"],"answer":"ジャンプボール"},

{"q":"１３．ドリブルを一度止めた後、もう一度ドリブルをすると何という？","choices":["トラベリング","ダブルドリブル","チャージング","バックコート"],"answer":"ダブルドリブル"},

{"q":"１４．ボールを持ったまま３歩以上歩く反則は？","choices":["ファウル","トラベリング","バックコート","キックボール"],"answer":"トラベリング"},

{"q":"１５．３ポイントラインの外からシュートが入ると何点？","choices":["1点","2点","3点","4点"],"answer":"3点"},

{"q":"１６．相手を押したりぶつかったりしてはいけない理由は？","choices":["ファウルになるから","点数が減るから","退場になるから","時計が止まるから"],"answer":"ファウルになるから"},

{"q":"１７．バックコートバイオレーションとは？","choices":["後ろ向きに走ること","前に運んだボールを自陣へ戻すこと","ボールを高く投げること","コートの外へ出ること"],"answer":"前に運んだボールを自陣へ戻すこと"},

{"q":"１８．試合中、コート内でプレーできる人数は？","choices":["4人","5人","6人","7人"],"answer":"5人"},

{"q":"１９．フリースローラインから打つシュートを何という？","choices":["レイアップ","フリースロー","ダンク","ジャンプシュート"],"answer":"フリースロー"},

{"q":"２０．ボールを持たずに味方へ道を作る動きを何という？","choices":["スクリーン","リバウンド","スティール","ドライブ"],"answer":"スクリーン"},

{"q":"２１．シュートが外れたボールを取ることを何という？","choices":["リバウンド","アシスト","ドライブ","ターンオーバー"],"answer":"リバウンド"},

{"q":"２２．味方のシュートにつながるパスを何という？","choices":["ドリブル","アシスト","リバウンド","チャージ"],"answer":"アシスト"},

{"q":"２３．相手のパスやドリブルを奪うことを何という？","choices":["ブロック","スティール","リバウンド","スクリーン"],"answer":"スティール"},

{"q":"２４．シュートを打つ相手のボールをはたき落とすプレーを何という？","choices":["アシスト","スティール","ブロック","スクリーン"],"answer":"ブロック"},

{"q":"２５．ドリブルをしながらゴールへ向かうプレーを何という？","choices":["ドライブ","リバウンド","チャージ","ジャンプボール"],"answer":"ドライブ"},

{"q":"２６．リングとバックボードを合わせて何という？","choices":["ゴール","ネット","バスケット","リング"],"answer":"バスケット"},

{"q":"２７．試合中、審判の笛が鳴ったらどうする？","choices":["プレーを止める","走り続ける","シュートを打つ","ドリブルを続ける"],"answer":"プレーを止める"},

{"q":"２８．試合前に一番大切なことは？","choices":["あいさつ","昼寝","ゲーム","おしゃべり"],"answer":"あいさつ"},

{"q":"２９．チームプレーで一番大切なのは？","choices":["協力","自分だけでプレー","文句を言う","あきらめる"],"answer":"協力"},

{"q":"３０．キングフィッシャーズの選手として大切なのは？","choices":["仲間を応援する","文句を言う","あきらめる","一人でプレーする"],"answer":"仲間を応援する"},
]

# -------------------------------
# 初回だけシャッフル
# -------------------------------
if "questions" not in st.session_state:
    shuffled = questions.copy()
    random.shuffle(shuffled)
    st.session_state.questions = shuffled

# -------------------------------
# 初期化
# -------------------------------
if "i" not in st.session_state:
    st.session_state.i = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.correct = False

# -------------------------------
# 終了画面
# -------------------------------
if st.session_state.i >= len(st.session_state.questions):

    st.balloons()

    st.success("🎉 お疲れさまでした！")

    st.write(
        f"## 得点：{st.session_state.score} / {len(st.session_state.questions)}"
    )

    percentage = st.session_state.score / len(st.session_state.questions) * 100
    st.write(f"### 正解率：{percentage:.0f}%")

    if st.button("もう一回"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    st.stop()

# -------------------------------
# 進捗バー
# -------------------------------
progress = st.session_state.i / len(st.session_state.questions)
st.progress(progress)

st.write(
    f"### 問題 {st.session_state.i + 1} / {len(st.session_state.questions)}"
)

# -------------------------------
# 問題表示
# -------------------------------
q = st.session_state.questions[st.session_state.i]

st.subheader(q["q"])

answer = st.radio(
    "答えを選んでください",
    q["choices"],
    key=f"q{st.session_state.i}"
)

# -------------------------------
# 回答前
# -------------------------------
if not st.session_state.answered:

    if st.button("回答する"):

        st.session_state.answered = True

        if answer == q["answer"]:
            st.session_state.score += 1
            st.session_state.correct = True
        else:
            st.session_state.correct = False

        st.rerun()

# -------------------------------
# 回答後
# -------------------------------
else:

    if st.session_state.correct:
        st.success("🎉 正解です！")
    else:
        st.error(f"❌ 不正解！ 正解は「{q['answer']}」です。")

    st.write(f"現在の得点：**{st.session_state.score}点**")

    if st.button("次の問題へ"):
        st.session_state.i += 1
        st.session_state.answered = False
        st.rerun()

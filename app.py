import streamlit as st

st.set_page_config(page_title="キングフィッシャーズ検定", page_icon="🏀")

st.title("🏀 バスケット検定")

questions = [
    {"q":"１．１試合、何Ｑ（クォーター）ある？","choices":["２Ｑ","３Ｑ","４Ｑ","６Ｑ"],"answer":"４Ｑ"},
    {"q":"２．ショットクロックは何秒？","choices":["１２秒","２４秒","３０秒","３６秒"],"answer":"２４秒"},
    {"q":"３．フリースローが１本入ったら何点？","choices":["１点","２点","３点","４点"],"answer":"１点"},
    {"q":"４．タイムアウトは何秒？※ミニバス公式ルールとして","choices":["３０秒","４５秒","６０秒","８０秒"],"answer":"６０秒"},
    {"q":"５．スローインの際、何秒以内にパスを出さなければならない？","choices":["３秒","４秒","５秒","６秒"],"answer":"５秒"},
    {"q":"６．フリースローはボールを渡されてから何秒以内にシュートを打たなければならない？","choices":["３秒","５秒","８秒","１０秒"],"answer":"５秒"},
    {"q":"７．パスを受けてから何秒以内にシュート・パス・ドリブルのいずれかを行わなければならない？","choices":["２秒","３秒","４秒","５秒"],"answer":"５秒"},
    {"q":"８．オフェンスがペイントエリア内に何秒以上、居座ってはいけない？","choices":["２秒","３秒","５秒","１０秒"],"answer":"３秒"},
    {"q":"９．１試合で同じ選手が何回ファウルしたら退場になる？","choices":["３回","４回","５回","退場にならない"],"answer":"５回"},
    {"q":"１０．コートに入れる人数は１チーム何人？","choices":["4人","5人","6人","7人"],"answer":"5人"},
]

# 初期化
if "i" not in st.session_state:
    st.session_state.i = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.correct = False

# 終了画面
if st.session_state.i >= len(questions):
    st.balloons()
    st.success(f"🎉 お疲れさまでした！")
    st.write(f"## 得点：{st.session_state.score} / {len(questions)}")

    if st.button("もう一度挑戦する"):
        st.session_state.i = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.correct = False
        st.rerun()

    st.stop()

q = questions[st.session_state.i]

st.subheader(q["q"])

answer = st.radio(
    "答えを選んでください",
    q["choices"],
    key=f"q{st.session_state.i}"
)

# 回答前
if not st.session_state.answered:

    if st.button("回答する"):

        st.session_state.answered = True

        if answer == q["answer"]:
            st.session_state.score += 1
            st.session_state.correct = True
        else:
            st.session_state.correct = False

        st.rerun()

# 回答後
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

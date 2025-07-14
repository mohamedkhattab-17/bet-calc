import streamlit as st

st.set_page_config(page_title="2-Way Betting Calculator", layout="centered")
st.markdown("""
    <style>
        .main {
            background: linear-gradient(white, lightblue);
            padding: 2rem;
            border-radius: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎲 2-Way Betting Calculator")

# Input fields
investment = st.number_input("Enter Total Investment (EUR):", min_value=0.0, format="%.2f")
odd1 = st.number_input("Enter Odds for Team 1:", min_value=0.01, format="%.2f")
odd2 = st.number_input("Enter Odds for Team 2:", min_value=0.01, format="%.2f")

# Calculation and output
if st.button("Calculate Bets"):
    try:
        R = investment / (1/odd1 + 1/odd2)
        bet1 = R / odd1
        bet2 = R / odd2
        profit = R - investment

        st.markdown(f"**Common Return (R):** €{R:.2f}")
        st.markdown(f"**Bet on Team 1:** €{bet1:.2f}")
        st.markdown(f"**Bet on Team 2:** €{bet2:.2f}")
        st.markdown(f"**Total Bet:** €{bet1 + bet2:.2f}")

        if R < investment:
            st.error(f"⚠️ Not a good deal — Guaranteed Loss: €{profit:.2f}")
        else:
            st.success(f"✅ Guaranteed Profit: €{profit:.2f}")

    except Exception as e:
        st.error("An error occurred. Please check your inputs.")

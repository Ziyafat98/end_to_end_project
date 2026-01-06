

import streamlit as st
import pandas as pd
from joblib import load
import calendar

# --------------------------------------------------
# Load trained model (cached to avoid reloading)
# --------------------------------------------------
@st.cache_resource(show_spinner="Loading model...")
def load_model():
    model = load("model_new.saleslib")
    return model
# --------------------------------------------------
# Make prediction based on user inputs
# --------------------------------------------------
def make_prediction(model):
    year = st.session_state["year"]
    month = st.session_state["month"]
    temp = st.session_state["temp"]
    store = st.session_state["store"]
    days_option = st.session_state["days_option"]
# If user selects a specific day

    if days_option == "Specific day":
        day = st.session_state["day"]
        X_pred = pd.DataFrame({
            "year": [year],
            "month_num": [month],
            "day_num": [day],
            "temperature_2m_mean": [temp],
            "store_id": [store]
        })
        pred = model.predict(X_pred)
        st.session_state["pred"] = round(float(pred[0]), 2)
    else:  
    # Whole month
        days_in_month = calendar.monthrange(year, month)[1]
        X_pred = pd.DataFrame({
            "year": [year]*days_in_month,
            "month_num": [month]*days_in_month,
            "day_num": list(range(1, days_in_month+1)),
            "temperature_2m_mean": [temp]*days_in_month,
            "store_id": [store]*days_in_month
        })
        preds = model.predict(X_pred)
        total_sales = preds.sum()
        st.session_state["pred"] = round(float(total_sales), 2)
# --------------------------------------------------
# Streamlit App Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    st.title("Store Sales Prediction")
# Load the ML model
    model = load_model()
 # Initialize prediction value
    if "pred" not in st.session_state:
        st.session_state["pred"] = None

    with st.form("form"):
        col1, col2, col3 = st.columns(3)

       # Left column: Year and Month inputs
        with col1:
            st.number_input("Year", min_value=2023, max_value=2030, value=2024, key="year")
            st.number_input("Month", min_value=1, max_value=12, value=1, key="month")

        # Middle column: Day option and temperature
        with col2:
            st.selectbox(
                "Days Option",
                options=["Specific day", "Whole month"],
                key="days_option"
            )
        # Show day selector only if "Specific day" is chosen
            if st.session_state["days_option"] == "Specific day":
                st.number_input("Select Day", min_value=1, max_value=31, value=1, key="day")
            st.number_input("Temperature (°C)", value=20.0, key="temp")

       # Right column: Store selection
        with col3:
            st.selectbox(
                "Store ID",
                options=[3, 5, 8],
                key="store"
            )
       # Submit button triggers prediction
        st.form_submit_button(
            "Calculate",
            type="primary",
            on_click=make_prediction,
            kwargs=dict(model=model)
        )
# --------------------------------------------------
    # Display prediction result
    # --------------------------------------------------
    if st.session_state["pred"] is not None:
        if st.session_state["days_option"] == "Specific day":
            st.subheader(f"Predicted Sales for {st.session_state['month']}/{st.session_state['day']}: {st.session_state['pred']}")
        else:
            st.subheader(f"Total Predicted Sales for Month {st.session_state['month']}: {st.session_state['pred']}")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from joblib import load

# ---------------- LOAD DATA ----------------

st.title("📈 Sales Trend with Predicted End")

# ====== LOAD DATA ======
@st.cache_data
def load_real_data():
    df = pd.read_excel("sales_merged.xlsx")
    df["date"] = pd.to_datetime(df["date"])
    return df

real_df = load_real_data()

# ====== LOAD MODEL ======
@st.cache_resource
def load_model():
    model = load("model_new.saleslib")
    return model

model = load_model()

# ====== PREDICT ======
X = real_df[["year", "month_num", "day_num", "temperature_2m_mean", "store_id"]]
real_df["predicted_sales"] = model.predict(X)

# ===== STREAMLIT DÜYMƏLƏR =====
store = st.selectbox("Store seç", real_df["store_id"].unique())
year = st.selectbox("İl seç", real_df["year"].unique())

plot_df = real_df[(real_df["store_id"] == store) & (real_df["year"] == year)]
plot_df = plot_df.sort_values("date").reset_index(drop=True)
plot_df["month"] = plot_df["date"].dt.strftime("%b")

# ===== SALES VƏ PREDICT DİZİLƏRİ =====
sales = plot_df["total_sales"].tolist()
pred = plot_df["predicted_sales"].tolist()
months = plot_df["month"].tolist()

# ===== QIRIQ-QIRIQ PREDICT XƏTT =====
predict_start = -3  # Son 3 ay predict kimi göstərilsin

fig, ax = plt.subplots(figsize=(10,5))

# REAL XƏTT
ax.plot(months[:predict_start], sales[:predict_start], color="blue", linewidth=2, label="Sales")

# SON HİSSƏ – PREDICT QIRIQ XƏTT
ax.plot(months[predict_start-1:], pred[predict_start-1:], color="orange",
        linewidth=2, linestyle=(0, (5, 5)), label="Predicted")  # (dash pattern)

ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.set_title(f"Store {store} Sales Trend – {year}")
ax.legend()
ax.grid(True)

st.pyplot(fig)
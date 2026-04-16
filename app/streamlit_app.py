import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import streamlit as st
import matplotlib.pyplot as plt
from src.data_preprocessing import preprocess
st.set_page_config(page_title="Climate Trend Analyzer", layout="wide")

st.title("🌍 Climate Trend Analyzer")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:

    # ---------------- LOAD + PROCESS ----------------
    df = preprocess(uploaded_file)

    # normalize country
    df['country'] = df['country'].astype(str).str.strip()

    st.success("Data loaded successfully")

    # ---------------- DEBUG (keep until stable) ----------------
    with st.expander("Debug Data"):
        st.write(df.head())
        st.write("Columns:", df.columns.tolist())
        st.write("Countries sample:", df['country'].value_counts().head(10))

    # ---------------- FILTER ----------------
    countries = sorted(df['country'].unique())

    selected_country = st.selectbox(
        "Select Country",
        countries,
        index=countries.index("India") if "India" in countries else 0
    )

    country_df = df[df['country'] == selected_country]

    # ---------------- GLOBAL DATA ----------------
    global_df = df.groupby('date', as_index=False)['value'].mean()
    global_df['moving_avg'] = global_df['value'].rolling(7, min_periods=1).mean()

    # =====================================================
    # 1. LINE GRAPH (TREND COMPARISON)
    # =====================================================
    st.subheader("📈 Line Chart: Country vs Global Trend")

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(country_df['date'], country_df['value'], label=f"{selected_country}", alpha=0.6)
    ax.plot(country_df['date'], country_df['moving_avg'], linestyle="--")

    ax.plot(global_df['date'], global_df['value'], label="Global Avg", color="black")
    ax.plot(global_df['date'], global_df['moving_avg'], linestyle="--", color="gray")

    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature")
    ax.legend()

    st.pyplot(fig)

    # =====================================================
    # 2. BAR GRAPH (YEARLY COMPARISON)
    # =====================================================
    st.subheader("📊 Bar Chart: Yearly Average")

    yearly_country = country_df.groupby('year')['value'].mean()
    yearly_global = df.groupby('year')['value'].mean()

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.bar(yearly_country.index, yearly_country.values, alpha=0.6, label=selected_country)
    ax.plot(yearly_global.index, yearly_global.values, color="black", marker="o", label="Global Avg")

    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature")
    ax.legend()

    st.pyplot(fig)

    # =====================================================
    # 3. PIE CHART (DATA DISTRIBUTION)
    # =====================================================
    st.subheader("🥧 Pie Chart: Country Distribution")

    top_countries = df['country'].value_counts().head(8)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(top_countries.values, labels=top_countries.index, autopct='%1.1f%%')

    st.pyplot(fig)
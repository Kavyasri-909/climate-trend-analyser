# 🌍 Climate Trend Analyzer

An interactive data analytics dashboard built with Python and Streamlit to explore historical climate data and visualize temperature trends across countries over time.

---

## 📌 Project Overview

This project analyzes global temperature datasets and transforms raw climate data into meaningful insights using data preprocessing, feature engineering, and interactive visualizations.

It focuses on comparing **country-level climate trends vs global averages**, helping understand long-term temperature changes.

---

## 🎯 Objectives

- Clean and standardize real-world climate datasets
- Handle inconsistent data formats across CSV files
- Build reusable data preprocessing pipeline
- Visualize climate trends using interactive charts
- Compare India vs Global temperature patterns

---

## ⚙️ Features

- 📂 Upload CSV dataset (dynamic input)
- 🧹 Automatic data cleaning & preprocessing
- 📈 Line chart: Temperature trends over time
- 📊 Bar chart: Yearly average temperature analysis
- 🥧 Pie chart: Country-wise data distribution
- 🌍 India vs Global climate comparison
- 🔍 Debug panel for dataset inspection

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas 📊
- Matplotlib 📈
- Streamlit ⚡

---

## 📁 Project Structure


climate trend analyser/
│
├── app/
│ └── streamlit_app.py
│
├── src/
│ ├── data_preprocessing.py
│ ├── utils.py
│ ├── anomaly_detection.py
│ ├── forecasting.py
│ └── feature_engineering.py
│
├── data/
├── models/
├── notebooks/
├── reports/
│
├── requirements.txt
└── README.md


---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/climate-trend-analyzer.git
cd climate-trend-analyzer
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run Streamlit app
streamlit run app/streamlit_app.py
📊 Key Insights
Temperature trends vary significantly across countries
Global average smooths out extreme regional variations
Data preprocessing is the most critical step in real-world analytics pipelines
⚠️ Challenges Faced
Handling inconsistent dataset formats (dt vs date)
Managing missing or null temperature values
Fixing module import issues in multi-folder project structure
Ensuring stable Streamlit execution across environments
💡 Learnings
Importance of data cleaning before visualization
Building modular data pipelines in Python
Debugging real-world dataset issues
Structuring a multi-folder analytics project
📌 Future Improvements
Add climate forecasting using ML models
Detect temperature anomalies over time
Add region-wise filtering and maps
Deploy dashboard on cloud (Streamlit Cloud / Render)

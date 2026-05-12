
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# --------------------------------
# PAGE CONFIG
# --------------------------------
st.set_page_config(
    page_title="AI Fraud Detection Dashboard",
    page_icon="💳",
    layout="wide"
)

# --------------------------------
# CUSTOM CSS
# --------------------------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3, h4 {
    color: white;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #333;
}

.block-container {
    padding-top: 2rem;
}

[data-testid="stSidebar"] {
    background-color: #1A1C24;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# LOAD MODEL
# --------------------------------
model = joblib.load(
    "fraud_detection_model.pkl"
)

# --------------------------------
# SIDEBAR
# --------------------------------
st.sidebar.title("🧠 Project Information")

st.sidebar.markdown("""
## AI-Powered Fraud Detection

This dashboard uses:

- 🤖 Random Forest Classifier
- 🧬 CTGAN Synthetic Data
- 📊 Fraud Probability Analysis
- 📈 Machine Learning Dashboard

---

### Features

✅ Fraud Detection  
✅ Synthetic Data Augmentation  
✅ Risk Analysis  
✅ Downloadable Reports  
✅ Interactive Dashboard  

---
""")

# --------------------------------
# MAIN TITLE
# --------------------------------
st.title("💳 AI Fraud Detection Dashboard")

st.markdown("""
Analyze uploaded financial transaction datasets and identify potentially fraudulent activities using Machine Learning and CTGAN-generated synthetic fraud data.
""")

# --------------------------------
# FILE UPLOADER
# --------------------------------
uploaded_file = st.file_uploader(
    "📂 Upload Transaction CSV File",
    type=["csv"]
)

# --------------------------------
# PROCESS FILE
# --------------------------------
if uploaded_file is not None:

    # Read CSV
    data = pd.read_csv(uploaded_file)

    # --------------------------------
    # REMOVE CLASS COLUMN IF EXISTS
    # --------------------------------
    if 'Class' in data.columns:
        data = data.drop('Class', axis=1)

    # --------------------------------
    # DATASET PREVIEW
    # --------------------------------
    st.subheader("📋 Uploaded Dataset Preview")

    st.dataframe(
        data.head(),
        use_container_width=True
    )

    st.info(
        f"Dataset contains {data.shape[0]} transactions and {data.shape[1]} features."
    )

    # --------------------------------
    # RUN MODEL
    # --------------------------------
    if st.button("🚀 Run Fraud Detection"):

        try:

            # --------------------------------
            # INPUT ARRAY
            # --------------------------------
            input_array = data.values

            # --------------------------------
            # PREDICTIONS
            # --------------------------------
            predictions = model.predict(input_array)

            probabilities = model.predict_proba(
                input_array
            )[:,1]

            # --------------------------------
            # RESULTS
            # --------------------------------
            results = pd.DataFrame({

                'Transaction_ID': range(
                    1,
                    len(predictions)+1
                ),

                'Fraud_Probability (%)': (
                    probabilities * 100
                ).round(2)

            })

            results['Prediction'] = predictions

            results['Prediction'] = results[
                'Prediction'
            ].map({
                0: 'Normal',
                1: 'Fraud'
            })

            # --------------------------------
            # RISK LEVEL
            # --------------------------------
            def risk_level(prob):

                if prob < 30:
                    return "🟢 Low"

                elif prob < 70:
                    return "🟠 Medium"

                else:
                    return "🔴 High"

            results['Risk_Level'] = results[
                'Fraud_Probability (%)'
            ].apply(risk_level)

            # --------------------------------
            # METRICS
            # --------------------------------
            fraud_count = (
                results['Prediction'] == 'Fraud'
            ).sum()

            normal_count = (
                results['Prediction'] == 'Normal'
            ).sum()

            total_transactions = len(results)

            fraud_percentage = (
                fraud_count / total_transactions
            ) * 100

            avg_probability = results[
                'Fraud_Probability (%)'
            ].mean()

            # --------------------------------
            # SUMMARY METRICS
            # --------------------------------
            st.subheader("📊 Fraud Detection Summary")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Total Transactions",
                total_transactions
            )

            col2.metric(
                "Fraud Detected",
                fraud_count
            )

            col3.metric(
                "Fraud Percentage",
                f"{fraud_percentage:.2f}%"
            )

            col4.metric(
                "Average Fraud Risk",
                f"{avg_probability:.2f}%"
            )

            # --------------------------------
            # ALERT
            # --------------------------------
            if fraud_count > 0:

                st.error(
                    f"🚨 ALERT: {fraud_count} potentially fraudulent transactions detected!"
                )

            else:

                st.success(
                    "✅ No fraudulent transactions detected."
                )

            # --------------------------------
            # SIDE BY SIDE CHARTS
            # --------------------------------
            st.subheader("📈 Fraud Analytics Dashboard")

            chart1, chart2 = st.columns(2)

            # --------------------------------
            # PIE CHART
            # --------------------------------
            with chart1:

                fig1, ax1 = plt.subplots(
                    figsize=(6,6)
                )

                ax1.pie(
                    [normal_count, fraud_count],
                    labels=['Normal', 'Fraud'],
                    autopct='%1.1f%%',
                    colors=['#36A2EB', '#FF4B4B'],
                    textprops={'fontsize': 12}
                )

                ax1.set_title(
                    "Fraud vs Normal Transactions",
                    fontsize=14
                )

                st.pyplot(fig1)

                plt.close(fig1)

            # --------------------------------
            # HISTOGRAM
            # --------------------------------
            with chart2:

                fig2, ax2 = plt.subplots(
                    figsize=(7,6)
                )

                ax2.hist(
                    results['Fraud_Probability (%)'],
                    bins=10,
                    color='#36A2EB',
                    edgecolor='white'
                )

                ax2.set_title(
                    "Fraud Risk Score Distribution",
                    fontsize=14
                )

                ax2.set_xlabel(
                    "Fraud Probability (%)"
                )

                ax2.set_ylabel(
                    "Transaction Count"
                )

                st.pyplot(fig2)

                plt.close(fig2)

            # --------------------------------
            # SUSPICIOUS TRANSACTIONS
            # --------------------------------
            st.subheader("🚨 Suspicious Transactions")

            suspicious = results[
                results['Prediction'] == 'Fraud'
            ]

            if len(suspicious) > 0:

                st.dataframe(
                    suspicious,
                    use_container_width=True
                )

            else:

                st.info(
                    "No suspicious transactions found."
                )

            # --------------------------------
            # FULL RESULTS
            # --------------------------------
            st.subheader("📝 Full Prediction Results")

            st.dataframe(
                results,
                use_container_width=True
            )

            # --------------------------------
            # DOWNLOAD BUTTON
            # --------------------------------
            csv = results.to_csv(index=False)

            st.download_button(
                label="⬇️ Download Results CSV",
                data=csv,
                file_name='fraud_detection_results.csv',
                mime='text/csv'
            )

        except Exception as e:

            st.error(
                f"❌ Error Processing File: {e}"
            )

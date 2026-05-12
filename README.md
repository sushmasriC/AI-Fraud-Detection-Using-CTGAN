# 💳 AI Fraud Detection Using CTGAN

<p align="center">
  <img src="screenshots/dashboard_home.png" width="100%" alt="Dashboard Preview">
</p>

<p align="center">
  <b>AI-Powered Fraud Detection using CTGAN Synthetic Data Generation and Machine Learning</b>
</p>

---

# 📌 Project Overview

This project focuses on enhancing financial fraud detection using **CTGAN-generated synthetic fraud transactions** and **Machine Learning**.

Financial fraud datasets are highly imbalanced, making fraud detection extremely challenging. To address this issue, synthetic fraud samples were generated using **CTGAN (Conditional Tabular GAN)** to augment the minority fraud class and improve model learning performance.

The project includes:

- Exploratory Data Analysis (EDA)
- Fraud pattern analysis
- Synthetic fraud generation using CTGAN
- Random Forest classification
- Model evaluation and comparison
- Interactive Streamlit dashboard deployment

---

# 🚀 Features

✅ Fraud Detection using Machine Learning  
✅ CTGAN-based Synthetic Fraud Generation  
✅ Interactive Streamlit Dashboard  
✅ Fraud Probability Analysis  
✅ Real vs Synthetic Fraud Comparison  
✅ Precision-Recall & ROC Curve Analysis  
✅ Downloadable Fraud Prediction Reports  
✅ Professional Visualization Dashboard  

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-learn | Machine Learning |
| CTGAN / SDV | Synthetic Data Generation |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Streamlit | Web Dashboard |
| Joblib | Model Serialization |
| Pyngrok | Public Dashboard Hosting |

---

# 📂 Dataset Information

The project uses the famous **Credit Card Fraud Detection Dataset** containing anonymized transaction features.

### Dataset Features

- `V1` to `V28` → PCA-transformed features
- `Time` → Transaction timestamp
- `Amount` → Transaction amount

### Target Variable

- `0` → Normal Transaction
- `1` → Fraudulent Transaction

---

# 📊 Exploratory Data Analysis

The following analyses were performed:

- Fraud vs Normal transaction distribution
- Transaction amount distribution
- Transaction time distribution
- Correlation heatmap
- Real vs Synthetic fraud comparison
- PCA visualization

---

# 🧬 Synthetic Fraud Generation using CTGAN

To overcome severe class imbalance:

1. Fraudulent transactions were isolated
2. CTGAN was trained on fraud samples
3. Synthetic fraud transactions were generated
4. Real and synthetic fraud data were combined
5. Augmented dataset was used for model training

This improved the model’s ability to learn rare fraud patterns more effectively.

---

# 🤖 Machine Learning Model

## Model Used

- Random Forest Classifier

## Training Strategy

Two models were compared:

| Model | Description |
|---|---|
| Baseline Model | Trained on original imbalanced dataset |
| Augmented Model | Trained using CTGAN synthetic fraud data |

---

# 📈 Model Performance

## Baseline Model

| Metric | Score |
|---|---|
| Accuracy | 99.95% |
| AUC Score | 0.9529 |
| Fraud Recall | 74% |

---

## Augmented Model

| Metric | Score |
|---|---|
| Accuracy | 99.95% |
| AUC Score | 0.9472 |
| Fraud Recall | 80% |

---

# 🔍 Key Observation

Although overall accuracy remained similar, the **fraud recall improved from 74% to 80%** after augmentation using CTGAN-generated synthetic fraud transactions.

This demonstrates that synthetic data augmentation helped the model better learn fraud patterns and improve fraud detection capability.

---

# 📸 Dashboard Features

The Streamlit dashboard allows users to:

- Upload transaction CSV datasets
- Run fraud detection instantly
- Analyze fraud probabilities
- Visualize fraud analytics
- View suspicious transactions
- Download prediction reports

---

# 📷 Dashboard Preview

## 🏠 Dashboard Home

<p align="center">
  <img src="screenshots/dashboard_home.png" width="100%">
</p>

---

## 📂 Uploaded Dataset Preview

<p align="center">
  <img src="screenshots/uploaded_dataset.png" width="100%">
</p>

---

## 📊 Fraud Detection Summary

<p align="center">
  <img src="screenshots/fraud_summary.png" width="100%">
</p>

---

## 📈 Fraud Analytics Dashboard

<p align="center">
  <img src="screenshots/charts.png" width="100%">
</p>

---

## 🚨 Suspicious Transactions

<p align="center">
  <img src="screenshots/suspicious_transactions.png" width="100%">
</p>

---

## 📝 Prediction Results

<p align="center">
  <img src="screenshots/prediction_results.png" width="100%">
</p>

---

# ▶️ Run Locally

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 2️⃣ Run Streamlit Application

```bash
streamlit run app.py
```

---

# 📂 Project Structure

```text
AI-Fraud-Detection-Using-CTGAN/
│
├── AI_Fraud_Detection_Using_CTGAN.ipynb
├── app.py
├── fraud_detection_model.pkl
├── scaler.pkl
├── ctgan_model.pkl
├── synthetic_fraud.csv
├── FINAL_WORKING_TEST.csv
├── requirements.txt
├── README.md
└── screenshots/
    ├── dashboard_home.png
    ├── uploaded_dataset.png
    ├── fraud_summary.png
    ├── charts.png
    ├── suspicious_transactions.png
    └── prediction_results.png
```

---

# 📌 Future Improvements

- Deep Learning-based fraud detection
- Real-time fraud monitoring
- Cloud deployment
- Explainable AI integration
- API integration for banking systems

---

# ✅ Conclusion

This project demonstrates how **CTGAN-generated synthetic fraud data** can improve fraud detection performance in highly imbalanced financial datasets.

By combining:

- Synthetic data generation
- Machine Learning
- Interactive dashboards

the system provides a practical and scalable AI-powered fraud detection solution.

---

# 👨‍💻 Author

## Chanda Sushmasri

AI & Data Science Enthusiast  
Machine Learning | Deep Learning | Data Analytics

---

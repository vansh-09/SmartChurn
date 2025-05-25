# 🚀 SmartChurn: Customer Churn Prediction with XGBoost

SmartChurn is a machine learning project designed to predict customer churn in the telecom sector using the XGBoost algorithm. This project demonstrates a full end-to-end pipeline — from data preprocessing to model explainability using SHAP — and extracts actionable business insights from the model.

---

## 🚀 Live Demo

🔗 [Click here to try SmartChurn in your browser](https://smartchurn-telco.streamlit.app/)  

---

## 📂 Dataset

- **Source:** [Telco Customer Churn Dataset (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  
- **Size:** 7,043 customer records  
- **Features:** Contract type, monthly charges, internet services, technical support, and more.

---

## ⚙️ Installation

```bash
git clone https://github.com/vansh-09/SmartChurn.git
cd SmartChurn
pip install -r requirements.txt
jupyter notebook
```

---

## 📈 Features Covered

- 📊 Exploratory Data Analysis (EDA)  
- 🧼 Data Cleaning & Feature Engineering  
- 🤖 Model training with XGBoost  
- ✅ Model evaluation using classification metrics  
- 🔍 Model interpretability using SHAP  
- 📉 Business insights generation  

---

## 🧪 Results

| Metric      | Value |
|-------------|-------|
| Accuracy    | ~84%  |
| Precision   | 83%   |
| Recall      | 87%   |
| F1-Score    | 85%   |

---

## 💡 Business Insights

- 📅 **Contract Type Matters**: Month-to-month customers are at highest risk of churn.  
- 🧾 **High Monthly Charges** correlate with churn unless bundled with extra services.  
- ❌ **Lack of Tech Support & Security Services** leads to higher churn.  
- 📄 **Paperless Billing Users** churn more — likely younger digital customers.  
- 📊 **Tenure Matters**: Customers with < 6 months tenure are most at risk.  

---

## 🗂️ Project Structure

```
SmartChurn/
├── data/                    # Telco dataset (telco.csv)
├── SmartChurn.ipynb         # Jupyter notebook
├── requirements.txt         # Python dependencies
├── Analysis_Report.md       # Business insights and documentation
├── .gitignore               # Ignored files
├── smartchurn_model.pkl     # Pickle file
└── README.md                # You're reading it!
```

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy, Matplotlib, Seaborn
- XGBoost
- SHAP
- Scikit-learn

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo, make changes, and open a pull request.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👋 Let's Connect

I'm open to collaboration, feedback, or internship opportunities!

- 📫 [LinkedIn](https://www.linkedin.com/in/vansh-codes/)  
- 📧 vanshkjain09@gmail.com

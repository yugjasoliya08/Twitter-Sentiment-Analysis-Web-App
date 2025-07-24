# 🐦 Twitter Sentiment Analysis Web App

Web-based Twitter Sentiment Analysis app using Python, NLP, Scikit-learn, VADER, and Streamlit for real-time sentiment prediction.

---

## 📌 Project Overview

- **Type**: Data Science, NLP, Web App  
- **Technology Stack**: Python, Streamlit, Scikit-learn, Pandas, TF-IDF  
- **Purpose**: Detect public sentiment from tweet-like texts using a trained machine learning model.

---

## 🚀 Features

- Real-time tweet sentiment prediction  
- Clean, interactive Streamlit web UI  
- Pretrained ML model using Logistic Regression  
- Text preprocessing and TF-IDF vectorization  
- Deployable on platforms like Streamlit Cloud or Heroku

---

## 📷 Screenshot

<img width="100%" alt="Streamlit Dashboard" src="https://github.com/user-attachments/assets/502bcc7f-bef3-4bfc-a86c-e1691655704a" />

---

## 🛠️ Technologies Used

| Category         | Tools & Libraries                       |
|------------------|-----------------------------------------|
| Programming      | Python                                  |
| Libraries        | Pandas, NumPy, Scikit-learn, Streamlit  |
| NLP              | TF-IDF, Text Cleaning, VADER            |
| Version Control  | Git, GitHub                             |

---

## 📁 Project Structure

```bash
Twitter-Sentiment-Analysis-Web-App/
├── app/                    # Streamlit web app files (app.py, model.pkl, vectorizer)
├── data/                   # Dataset used for training/testing
├── notebook/               # Jupyter notebooks for EDA, training, etc.
├── .ipynb_checkpoints/     # Auto-generated Jupyter checkpoints (ignored)
├── .gitignore              # Git ignore


## 🧑‍💻 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yugjasoliya08/Twitter-Sentiment-Analysis-Web-App.git
   cd Twitter-Sentiment-Analysis-Web-App
   
2.Create virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.Run the Streamlit app:
streamlit run app.py

5. ➕ Add Folder Descriptions to README Top Summary
 This project is divided into:
- `app/`: Streamlit frontend and model code
- `data/`: Dataset CSV for training
- `notebook/`: Exploratory analysis and training notebook

---
### ✅ **Add How It Works**
```markdown
## ⚙️ How It Works
1. User inputs a tweet-like message in the Streamlit web app.
2. Text is cleaned (lowercase, removing special characters, stopwords).
3. Preprocessed text is transformed using a pre-trained TF-IDF vectorizer.
4. Logistic Regression model predicts the sentiment.
5. Output is shown as **Positive**, **Negative**, or **Neutral**.


## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## 👨‍💻 Author
- **Yug Jasoliya**
- 📧 [Yugjasoliya49@gmail.com]
- 🔗 [LinkedIn Profile](https://linkedin.com/in/yugjasoliya)


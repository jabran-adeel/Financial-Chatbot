# 💬 AI-Powered Financial Chatbot (Flask Web App)

An interactive **AI-based financial chatbot** built using **Flask** and **Python**, designed to provide insights on key financial metrics for **Microsoft**, **Apple**, and **Tesla** based on real-world financial data (2022–2024).

This project is part of the **Boston Consulting Group (BCG) GenAI Job Simulation (The Forage)** — Task 2: *Developing an AI-Powered Financial Chatbot*.  
It showcases how generative AI and financial analytics can merge to create smart, data-driven conversational tools.

---

## 🚀 Features

✅ **Dynamic Financial Chatbot:**  
Ask natural-language questions like:
- “What is Microsoft’s revenue in 2024?”
- “How did Tesla’s revenue change between 2023 and 2024?”
- “What are Apple’s assets and liabilities for 2023?”
- “Show Microsoft’s cash flow.”

✅ **Rule-Based NLP Logic:**  
Understands predefined keywords and responds using structured financial data.

✅ **Data-Driven Insights:**  
Pulls real company data (Microsoft, Apple, Tesla) from `financial_data_2022_2024.csv`.

✅ **Web Interface (Flask):**  
Chat with the bot via a clean, responsive frontend (HTML + CSS + JavaScript).

✅ **Extensible Design:**  
Easily upgradeable to include Large Language Model (LLM) APIs like OpenAI or Gemini.

---

## 🧠 Project Overview

This chatbot demonstrates how AI and finance can combine to simplify complex data into human-like conversations.  
It uses **rule-based AI logic** for quick insights but is structured for future integration with advanced NLP or LLMs.

### 🔍 Tech Stack

| Category | Technologies Used |
|-----------|-------------------|
| Backend | Python, Flask |
| Data Handling | pandas |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Gunicorn + Procfile (for Heroku/Render) |
| Dataset | `financial_data_2022_2024.csv` (Microsoft, Apple, Tesla) |

---

## 🗂️ Project Structure

financial-chatbot/

├── app.py

├── bot_logic.py

├── data_loader.py

├── financial_data_2022_2024.csv

├── requirements.txt

├── Procfile

├── templates/

│ └── index.html

├── static/

│ └── styles.css

└── screenshots/

├── Screenshot_1.png

├── Screenshot_2.png

├── Screenshot_3.png

└── Screenshot_4.png


---

## ⚙️ Installation & Setup (Local)

Follow these easy steps to run it locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/financial-chatbot.git
cd financial-chatbot
```

## 2️⃣ Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate     # For Windows
# OR
source venv/bin/activate  # For Mac/Linux
```

## 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

## 4️⃣ Run the Flask app
```bash
python app.py
```

## 5️⃣ Open in browser

Go to 👉 `http://127.0.0.1:5000`

## 💻 Usage

Type a financial question in the chatbox such as:

`“What is Apple’s revenue 2023?”`

`“How much did Microsoft’s revenue grow?”`

`“Tesla assets and liabilities 2024?”`

and the chatbot will return clean, data-based answers.

## 🧾 Dataset Reference

The dataset `financial_data_2022_2024.csv` contains verified data for:

~Microsoft

~Apple

~Tesla

## Columns	Description
Company	Company name
Year	Fiscal year
Total Revenue (USD millions)	Company’s total revenue
Net Income (USD millions)	Company’s net income
Total Assets (USD millions)	Company’s total assets
Total Liabilities (USD millions)	Company’s total liabilities
Operating Cash Flow (USD millions)	Cash generated from operations


## 🧠 Example Queries
User Query	Chatbot Response Example
`“What is Microsoft revenue 2024?”`	Microsoft’s total revenue in 2024 was $245,122 million.
`“Apple net income 2023”`	Apple’s net income in 2023 was $96,995 million.
`“Tesla revenue growth”`	Tesla’s revenue increased by 1.0% from 2023 to 2024.
`“Apple assets and liabilities 2024”`	Apple had assets of $331,612M and liabilities of $308,030M in 2024.

## 👨‍💻 Author

**Jabran Adeel**

AI/ML Engineer • Data Scientist • Generative AI Developer

🔗 [GitHub](https://www.github.com/jabran-adeel/)
 | [LinkedIn](https://www.linkedin.com/in/jabran-adeel)
 | [Kaggle](https://www.kaggle.com/jabranadeel)

“AI is not replacing humans — it’s empowering them to make smarter decisions.”

`— Jabran Adeel`

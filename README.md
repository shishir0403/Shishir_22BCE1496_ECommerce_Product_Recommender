# 🛍️ E-Commerce Product Recommender System

An AI-powered web application that recommends similar or complementary products to users, built using **FastAPI**, **React**, and **Tailwind CSS**.

This project demonstrates full-stack development, database design, machine learning integration, and clean UI implementation — ideal for showcasing technical and practical skills for job selection.

---

## 🚀 Features

✅ AI-driven product recommendation system using embeddings and similarity scoring  
✅ RESTful API built with **FastAPI** and **SQLite** database  
✅ Frontend in **React + Tailwind CSS** for a clean, modern UI  
✅ Real product dataset with categories, prices, and descriptions  
✅ Realtime product fetching and recommendation display  
✅ Modular, scalable code structure (frontend + backend separation)

---

## 🧠 Tech Stack

### 🖥️ Frontend
- React (Vite)
- Tailwind CSS
- Fetch API

### ⚙️ Backend
- FastAPI
- SQLAlchemy + SQLite
- Pydantic
- Scikit-learn
- OpenAI API (for future LLM-based product description embeddings)

---

## 🗂️ Project Structure

ecommerce-recommender/
│
├── backend/
│ ├── app/
│ │ ├── main.py # FastAPI entry point
│ │ ├── db.py # Database connection + schema
│ │ ├── seed_data.py # Sample product dataset
│ │ ├── recommender.py # ML-based recommendation logic
│ │ ├── models.py # Data models
│ │ └── llm_adapter.py # (Optional) for LLM integration
│ └── database.db # SQLite database
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx # React entry point
│ │ ├── pages/Home.jsx # Main UI for product list + recommendations
│ │ ├── config.js # API base URL
│ │ └── index.css # Tailwind styles
│ ├── package.json
│ └── vite.config.js
│
└── README.md

yaml
Copy code

---

## ⚡ Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/ecommerce-recommender.git
cd ecommerce-recommender
2️⃣ Setup the Backend
bash
Copy code
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy scikit-learn pandas numpy python-dotenv
python
>>> from app.db import create_tables
>>> from app.seed_data import seed
>>> create_tables()
>>> seed()
>>> exit()
uvicorn app.main:app --reload
Server runs at:
👉 http://127.0.0.1:8000

3️⃣ Setup the Frontend
bash
Copy code
cd frontend
npm install
npm run dev
Frontend runs at:
👉 http://127.0.0.1:5173

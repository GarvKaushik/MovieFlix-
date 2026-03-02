## 🎬 MovieFlix – AI Movie Recommender System

MovieFlix is a full-stack AI-powered movie recommendation web application built using FastAPI, React, and Scikit-learn.
It recommends similar movies using content-based filtering and cosine similarity.

🚀 -- Features --

🔍 Search from existing movies (dropdown search)
🎯 Top 5 similar movie recommendations
🖼 Movie posters fetched dynamically from TMDB API
⚡ Fast cosine similarity computation (optimized)
🌐 Fully deployed frontend & backend

🧠-- How It Works --
1. Movie metadata is merged into a single tags column.
2. Text is vectorized using:
```
CountVectorizer(max_features=5000, stop_words="english")

```
3. Cosine similarity is computed dynamically:
```
cosine_similarity(vectors[index], vectors)
```
4. Top 5 most similar movies are returned.

5. Posters are fetched from the TMDB API.

## 🏗 Tech Stack
## Frontend
React
CSS
Fetch API

## Backend
FastAPI
Uvicorn
Python
Requests
Python-dotenv

## Machine Learning
Scikit-learn
CountVectorizer
Cosine Similarity
Pandas
NumPy

---📂 Project Structure ----
```
MovieFlix/
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── .env
│
├── backend/
│   ├── main.py
│   ├── vectors.pkl
│   ├── movies.pkl
│   ├── requirements.txt
│   └── runtime.txt
│
└── README.md
```

## ⚙️ Backend Setup (Local)
1. Navigate to backend
cd backend
2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
3. Install dependencies
pip install -r requirements.txt
4. Create .env file inside backend
TMDB_API_KEY=your_tmdb_api_key_here
5. Run server
uvicorn main:app --reload

Backend runs at:
```
http://127.0.0.1:8000
```
## ⚙️ Frontend Setup (Local)
1. Navigate to frontend
```cd frontend```
3. Install dependencies
```npm install```
4. Create .env file inside frontend
```REACT_APP_BACKEND_URI=http://127.0.0.1:8000```
5. Start frontend
```npm start```

Frontend runs at:

```
http://localhost:3000
```
📡 API Endpoints
Get All Movies
``GET /movies``

Response:
```
{
  "movies": ["Avatar", "Batman", "..."]
}
```
Get Recommendations
```GET /recommend/{movie_name}```

Response:
```
{
  "recommendations": [
    {
      "title": "Aliens",
      "poster": "https://image.tmdb.org/..."
    }
  ]
}
```
## 🌍 Deployment
--- Backend (Render)---

```Root Directory: backend```
Build Command:

```
pip install -r requirements.txt
```

Start Command:
```
uvicorn main:app --host 0.0.0.0 --port 10000
```
Add Environment Variable:

```TMDB_API_KEY```

--- Frontend (Vercel)---

```Root Directory: frontend```

Add Environment Variable:

```REACT_APP_BACKEND_URI=https://your-backend.onrender.com```

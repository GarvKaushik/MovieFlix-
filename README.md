🎬 MovieFlix – AI Movie Recommender System

MovieFlix is a full-stack AI-powered movie recommendation web application built using FastAPI, React, and Scikit-learn.
It recommends similar movies using content-based filtering and cosine similarity.

🚀 ## Features ##

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

----🏗 Tech Stack---
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

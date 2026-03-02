import pickle
import requests
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from functools import lru_cache
load_dotenv()
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TMDB_API_KEY = os.getenv("TMDB_API_KEY")


movies = pickle.load(open('movies.pkl', 'rb'))
vectors = pickle.load(open('vectors.pkl', 'rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url, timeout=5)
    data = response.json()
    poster_path = data.get('poster_path')

    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return None

@lru_cache(maxsize=500)
def fetch_main(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url, timeout=5)
    data = response.json()
    backdrop_path = data.get('backdrop_path')
   
    description = data.get('overview')
    poster_path = data.get('poster_path')
   
    if backdrop_path and description and poster_path:
        return {
            "backdrop": f"https://image.tmdb.org/t/p/w500/{backdrop_path}",
            "description": description,
            "poster-main": f"https://image.tmdb.org/t/p/w500/{poster_path}"
        }
    return None




def recommend(movie):
    movie = movie.lower()
    titles = movies['title'].str.lower()
    if movie not in titles.values:
        return []

    index = titles[titles == movie].index[0]
    main_id = movies.iloc[index].movie_id
    # distances = sorted(
    #     list(enumerate(similarity[index])),
    #     reverse=True,
    #     key=lambda x: x[1]
    # )[1:6]
    similarity_scores = cosine_similarity(
        vectors[index],
        vectors
    )[0]

  

    movies_list = similarity_scores.argsort()[-6:-1][::-1]

    recommendations = []
  
    for i in movies_list:
        movie_id = movies.iloc[i].movie_id

        recommendations.append({
            "title": movies.iloc[i].title,
            "poster": fetch_poster(movie_id),
         
        })
    recommendations.append({
           "backdrop": fetch_main(main_id)['backdrop'],
           "description": fetch_main(main_id)['description'],
           "poster_main": fetch_main(main_id)['poster-main']
    })
    return recommendations


@app.get("/movies")
def get_movies():
    return {"movies": movies['title'].tolist()}


@app.get("/recommend/{movie_name}")
def get_recommendations(movie_name: str):
    return {"recommendations": recommend(movie_name)}
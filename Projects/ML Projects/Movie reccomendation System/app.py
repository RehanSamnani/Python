import numpy as np
import pandas as pd
import streamlit as st
import requests

# Set page configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS for a more attractive Netflix-like theme
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1c1c1c;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 48px;
        color: #e50914;
        text-align: center;
        font-weight: bold;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
    .movie-title {
        font-size: 18px;
        color: #ffffff;
        text-align: center;
        margin-top: 10px;
        font-weight: bold;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.7);
    }
    .movie-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 10px;
        border: 2px solid #e50914;
        border-radius: 10px;
        padding: 10px;
        background-color: #2c2c2c;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    }
    .recommend-button {
        background-color: #e50914;
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .recommend-button:hover {
        background-color: #b20710;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a custom title
st.markdown('<h1 class="title">Movie Recommendation System 🎬</h1>', unsafe_allow_html=True)

# Load data
similarity = np.load(r"Data set/similarity.npy")
movies = pd.read_csv(r"Data set/final_movies_data.csv")

# Function to fetch the poster URL using TMDb API
def fetch_poster(movie_id):
    api_key = "efe3a50680b6996804cd662548a85286"  # Replace with your TMDb API key
    base_url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US"
    response = requests.get(base_url.format(movie_id, api_key))
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            full_poster_url = "https://image.tmdb.org/t/p/w500" + poster_path
            return full_poster_url
    return None

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    poster_urls = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        poster_urls.append(fetch_poster(movie_id))  # Fetch poster for each movie

    return recommended_movies, poster_urls

# Movie selection
option = st.selectbox(
    'Choose a movie',
    movies['title'].values,
)

# Update the button style
if st.button('Recommend', key='recommend_button', help='Click to get movie recommendations'):
    recommendations, posters = recommend(option)
    st.markdown('<h2 style="color:#e50914; text-align:center;">Recommended Movies</h2>', unsafe_allow_html=True)

    # Create rows of movies (5 movies per row)
    for i in range(0, len(recommendations), 5):
        cols = st.columns(5)
        for col, title, poster in zip(cols, recommendations[i:i+5], posters[i:i+5]):
            with col:
                if poster:
                    st.image(poster, use_container_width=True, width=150)
                st.markdown(f'<div class="movie-title">{title}</div>', unsafe_allow_html=True)

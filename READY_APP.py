import streamlit as st
import pandas as pd
import requests
import pickle
from huggingface_hub import hf_hub_download


@st.cache_resource

def load_data():
    movies_path = hf_hub_download(
        repo_id="theconqueror004/streamlit_ml_model",  # HF repo name
        filename="movies.pkl",
        token=st.secrets["HF_TOKEN"]  # Streamlit secret
    )
    similarity_path = hf_hub_download(
        repo_id="theconqueror004/streamlit_ml_model",
        filename="similarity.pkl",
        token=st.secrets["HF_TOKEN"]
    )
    movies=pickle.load(open(movies_path, "rb"))
    similarity=pickle.load(open(similarity_path, "rb"))
    return movies, similarity
movie_list, similarity = load_data()
api_key=st.secrets["TMDB_API_KEY"]
#fetch poster function
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        )
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception as e:
        st.warning(f"Could not fetch poster for movie ID {movie_id}. Error: {e}")
    return None

#recommendation function

def recommend(movie):
    movie_idx=movie_list[movie_list["title"].str.lower()==movie.lower()].index[0]
    distance=similarity[movie_idx]
    movie_list_sorted=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    reccommended_movie_posters=[]
    for i in movie_list_sorted:
        recommended_movies.append(movie_list.iloc[i[0]].title)
        reccommended_movie_posters.append(fetch_poster(movie_list.iloc[i[0]].id))
    return recommended_movies,reccommended_movie_posters

movie_samples=movie_list['title'].values
st.title("Movie Recommendation System")
st.write("Welcome to the Movie Recommendation System! Please enter your favorite movie to get recommendations.")

selected_movie_name = st.selectbox(
    'Movies List....Choose your favorite movie:',
    movie_samples
)
if st.button("Reccomend"):
    names, posters = recommend(selected_movie_name)
    cols=st.columns(5)
    for idx,col in enumerate(cols):
        with col:
            st.text(names[idx])
            if posters[idx]:
                st.image(posters[idx])
            else:
                st.write("Poster not available")

st.write(f"You selected: {selected_movie_name}")
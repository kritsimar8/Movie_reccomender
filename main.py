import streamlit as st
import pickle
import pandas as pd
import requests


def fetch (movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=636237cea5eeae05dad91957fcb330ea&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies =[]
    recommended_movies_poster=[]
    for i in movie_list:
        movie_id= movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch(movie_id))
    return recommended_movies,recommended_movies_poster



movies_dict = pickle.load(open('movie_dict1.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pickle','rb'))

st.title('Movie recommender system ')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values )
if st.button('Recommend'):
    names,poster = recommend(selected_movie_name)

    col1, col2, col3 , col4, col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
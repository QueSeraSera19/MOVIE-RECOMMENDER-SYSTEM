import streamlit as st
import pickle
import pandas as pd
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        movie_id=i[0]
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('movie recommender system')
selected_movie = st.selectbox(
    "Select Movie",
   movies['title'].values
)

st.write("You selected:", selected_movie)
if st.button("Recommend"):
    recommendations=recommend(selected_movie)
    for i in recommendations:
        st.write(i)


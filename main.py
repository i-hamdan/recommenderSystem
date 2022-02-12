import pickle

import streamlit as st
import requests


# THIS IS THE CODING PART

matrix = pickle.load(open('recoMatrix__v1.0.pkl', 'rb'))
movies = matrix['title'].values

def selectedOption(option):
    return matrix.loc[matrix['title'] == option]

def findSimilar(row):
    return [x for x in row]







# THIS IS THE DISPLAYED PART
st.title('Movie Recommender System')

col1, col2 = st.columns(2)

with col1:
    option = st.selectbox(
        'Please select a Movie',
        movies
    )
    selectedDetails = selectedOption(option)
    st.write(selectedDetails.iloc[0, 2])
    listMovies = [x[1] for x in findSimilar(selectedDetails.iloc[0, -1])]
    listPosters = [x[-1] for x in findSimilar(selectedDetails.iloc[0, -1])]

with col2:
    st.write('')
    st.write('')
    url = selectedDetails.iloc[0,3]
    st.image(url, width=300)

if st.button('Recommend'):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(listPosters[0], caption=listMovies[0])
    with col2:
        st.image(listPosters[1], caption=listMovies[1])
    with col3:
        st.image(listPosters[2], caption=listMovies[2])
    with col4:
        st.image(listPosters[3], caption=listMovies[3])
    with col5:
        st.image(listPosters[4], caption=listMovies[4])





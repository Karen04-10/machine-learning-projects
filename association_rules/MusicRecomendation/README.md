# Song Recommendation System

## Project Type
Content-Based Recommendation System (Association Rule Learning)

## Description
A music recommendation system that suggests songs similar to a selected track based on their audio features and genres. The project combines standardized audio characteristics with multi-label genre encoding and uses the K-Nearest Neighbors (KNN) algorithm with cosine similarity to find the most relevant recommendations.

## Dataset
Songs dataset containing: artist,song,duration_ms,explicit,year,popularity,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,genre

## Skills & Tools
- Pandas
- Scikit-learn
- SciPy

## How to Run
1. Install the required dependencies.
2. Place songs.csv inside the data/ folder.
3. Open and run the notebook.

## Results
The system returns the most similar songs.
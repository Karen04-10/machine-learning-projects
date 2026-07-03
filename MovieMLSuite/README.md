# Movie ML Suite

## Project Type
Regression, Classification, Recommendation Systems, EDA, ANN

## Description
MovieMLSuite is a complete machine learning project built on a movies dataset. It includes multiple data science workflows such as data cleaning, exploratory data analysis, predictive modeling, and a movie recommendation system. The project demonstrates both supervised learning (classification & regression) and unsupervised/content-based recommendation techniques.

## Dataset
Movies dataset (movies.csv) containing:
Movie, Director, Running time, Actor 1, Actor 2, Actor 3, Genre,Budget, Box Office, Actors Box Office %, Director Box Office %, Earnings, Oscar and Golden Globes nominations, Oscar and Golden Globes awards, Release year,IMDb score

## Skills & Tools
- Pandas
- Matplotlib / Seaborn
- Scikit-learn
- Tensorflow
- XGBoost
- WordCloud
- Nltk
- SciPy

## Project Modules
1. Data Cleaning   (dfClearing.py)
Handling missing values
Removing duplicates
2. Exploratory Data Analysis (EDA)   (ExploratoryDataAnalysis.ipynb)
Data visualization
Distribution analysis
Correlation insights
Feature relationships
3. Hit / Flop Prediction   (HitFlop.ipynb)
Classification model to predict whether a movie is successful or not
4. IMDb Rating Prediction   (IMDp_Prediction.ipynb)
Regression model to predict movie ratings
5. Profit Prediction   (ProfitPrediction.ipynb)
Regression-based prediction of movie profitability
6. Movie Recommendation System   (MovieRecommendation.ipynb)
Content-based filtering using movie features
Similarity-based recommendation approach

## Project Structure
MovieMLSuite/
│
├── data/
│   └── movies.csv
├── utils/
│   └── dfCleaning.py
├── notebooks/
│   ├── EDA.ipynb
│   ├── HitFlop.ipynb
│   ├── IMDb_prediction.ipynb
│   ├── MovieRecommendation.ipynb
│   └── ProfitPrediction.ipynb
├── README.md
└── requirements.txt

## How to Run
1. Clone the repository
2. Install dependencies:
3. Open notebooks inside notebooks/ folder
4. Run notebooks in order:
EDA.ipynb
HitFlop.ipynb
IMDb_prediction.ipynb
MovieRecommendation.ipynb
ProfitPrediction.ipynb

## Results
- Clean and structured movie dataset
- Insights from EDA
- Classification model for Hit/Flop prediction
- Regression models for IMDb rating and profit prediction
- Content-based movie recommendation system
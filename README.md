Overview

This project predicts house prices in California using K-Nearest Neighbors (KNN) regression. It analyzes the factors influencing housing prices and provides accurate predictions using machine learning techniques.

Dataset

The dataset contains California housing data with the following columns:

median_income: Median income of households in the area

housing_median_age: Median age of the houses

total_rooms: Total number of rooms

population: Total population of the block

latitude: Latitude coordinate of the house

longitude: Longitude coordinate of the house

median_house_value: Target variable representing house price

Objectives

Predict median house values in California

Identify key features influencing house prices

Perform exploratory data analysis (EDA) to understand trends and patterns

Build and evaluate a KNN regression model for price prediction

Approach

Data Cleaning & Preprocessing

Handle missing values and duplicates

Feature scaling and transformation

Split dataset into training and testing sets

Exploratory Data Analysis (EDA)

Visualize distributions of features

Correlation analysis

Feature vs. target visualizations

Detect and handle outliers

Modeling

Implement K-Nearest Neighbors (KNN) regression

Hyperparameter tuning using GridSearchCV

Evaluation

Metrics used: RMSE, MAE, R² score

Compare predicted vs. actual house prices

Tools & Libraries

Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn

Results

KNN regression provided competitive accuracy in predicting housing prices

Median income and location were the most influential features

Future Work

Experiment with advanced regression models like Random Forest or XGBoost

Deploy the model using Flask or Streamlit

Build interactive dashboards for visual exploration of housing data

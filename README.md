🏡 California House Price Prediction (KNN)

🎯 Business Problem
The California real estate market is highly dynamic, with housing prices influenced by location, income levels, and property features. Buyers struggle to make informed decisions, sellers face challenges in pricing competitively, and investors require reliable property valuation for financing. Traditional valuation methods based on heuristics or historical averages are often inefficient, non-scalable, and error-prone, leading to mispriced properties, prolonged sales, and suboptimal investments. A data-driven approach using KNN regression can provide accurate price predictions to minimize financial risks and improve decision-making for all stakeholders.

📌 Overview
This project predicts house prices in California using K-Nearest Neighbors (KNN) regression. It includes data preprocessing, exploratory data analysis (EDA), feature engineering, and model evaluation to understand factors influencing house prices.

📂 Dataset
The dataset contains California housing data with the following columns:

median_income: Median income of households

housing_median_age: Median age of the houses

total_rooms: Total number of rooms

population: Total population of the block

latitude: Latitude of the house

longitude: Longitude of the house

median_house_value: Target variable representing house price

⚙️ Approach

Data Preprocessing: Handle missing values, scale features, split train/test sets

EDA: Analyze distributions, correlations, feature-target relationships, detect outliers

Modeling: Implement KNN regression with hyperparameter tuning

Evaluation: Metrics used include RMSE, MAE, and R² score; compare predicted vs. actual prices

📊 Results

KNN regression achieved competitive accuracy in predicting California house prices

Median income and location were the most influential features

# Site Selection for Solar Deployment – Data Science Assessment

## Overview

This project aims to identify optimal locations for solar energy deployment using a data-driven approach. By analyzing a combination of geographic, environmental, and socioeconomic features, we assess potential sites for solar infrastructure with the goal of maximizing efficiency and sustainability.

This is a data science assessment project that applies supervised machine learning techniques—**Random Forest** and **Logistic Regression**—to evaluate and classify site suitability.

## Objectives

- Develop a predictive model to classify locations as suitable or not suitable for solar deployment.
- Compare the performance of two classification algorithms: Random Forest and Logistic Regression.
- Identify the most important features influencing site selection decisions.

## Methodology

### Data Collection & Preprocessing

- Collected data from relevant open-source datasets, which include:
  - Solar irradiance
  - Land use
  - Infrastructure index
  - Population density
  - Electricity grid access
- Cleaned and preprocessed the data by handling missing values, encoding categorical variables, and normalizing numerical features.

### Model Development

Two classification models were developed:

1. **Logistic Regression**
   - Interpretable linear model
   - Applied One-vs-Rest (OvR) strategy with oversampling of the minority class
   - Achieved **~0.90 accuracy** with balanced performance across classes

2. **Random Forest Classifier**
   - Ensemble method using multiple decision trees
   - Achieved **~0.90 accuracy**, but failed to correctly identify any of the minority class
   - Performance was misleading due to class imbalance

### Evaluation Metrics

Models were evaluated based on:
- Accuracy
- Precision, Recall, and F1-score
- ROC-AUC score
- Confusion Matrix analysis

## Results

| Model              | Accuracy | Minority Class Recall | Comments                                   |
|-------------------|----------|------------------------|--------------------------------------------|
| Logistic Regression | 0.90     | Good                   | OvR + oversampling improved class balance  |
| Random Forest       | 0.90     | Poor                   | Failed to detect minority class cases      |

- **Logistic Regression** provided more reliable results under class imbalance using appropriate sampling and classification strategy.
- **Random Forest**, while scoring similarly on accuracy, was not useful due to complete failure in identifying the minority class.
- **Feature Importance Analysis** highlighted solar irradiance, land use, and infrastructure index as key drivers.


## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/solar-site-selection.git
   cd solar-site-selection
pip install -r requirements.txt



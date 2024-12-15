# Titanic Survival Prediction

This project involves predicting the survival of passengers aboard the Titanic using machine learning models. The dataset is sourced from Kaggle’s Titanic challenge, which provides a rich dataset for classification tasks.

## Project Overview
The goal of this project is to build a predictive model that determines whether a passenger survived the Titanic disaster. Two datasets are provided:

1. **train.csv**: Used for training the machine learning model. It includes features like age, gender, socio-economic class, etc., along with the survival status (0 = No, 1 = Yes).
2. **test.csv**: Used for making predictions. It contains the same features as `train.csv` but does not include the survival status.

The project also demonstrates effective data preprocessing techniques and the use of two machine learning models:

- Random Forest Classifier
- Logistic Regression Model

## Dataset Preprocessing
Key preprocessing steps include:
- Handling missing values using median or most frequent imputation.
- Encoding categorical variables like `Sex` and `Embarked`.
- Standardizing numeric features for consistent scaling.

## Model and Accuracy
The following models were used to predict survival:

1. **Random Forest Classifier**
   - Validation Accuracy: **81.56%**
2. **Logistic Regression (with clean preprocessing)**
   - Validation Accuracy: **80.45%**

## File Descriptions
- **train.csv**: Training dataset with passenger details and survival status.
- **test.csv**: Testing dataset for predictions.
- **titanic_predictions_clean_logistic.csv**: Final submission file with predicted survival status using the Logistic Regression model.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/titanic-survival-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd titanic-survival-prediction
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the prediction script:
   ```bash
   python predict.py
   ```

## Submission Format
The submission file is a CSV with the following format:

| PassengerId | Survived |
|-------------|----------|
| 892         | 0        |
| 893         | 1        |
| ...         | ...      |

- **PassengerId**: ID of the passenger from `test.csv`.
- **Survived**: Predicted survival status (0 = No, 1 = Yes).

## Technologies Used
- Python
- Pandas
- Scikit-learn

## Results
The Logistic Regression model with efficient preprocessing was chosen for the final submission due to its simplicity and competitive accuracy.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute or raise issues in this repository for improvements!


E E P 555 — Data Science for Machine Learning
Assignment 1
Total Points: 100
Winter Quarter, 2026
Department of Electrical and Computer Engineering
University of Washington, Seattle, WA
Due: Wednesday, January 28, 2026 (11:59 PM PT) via Canvas (as .ipynb)
Important Reference Notebooks (In-Class Demos)
For this assignment, refer to the following demo notebooks posted on Canvas:
Canvas→Files→In-Class-Demos

LinearvsPolynomialvsSinusoidalRegression.ipynb
RegressionCaseStudyStudentPerformance.ipynb
Submission & Format (Required)

You must submit asingle Python Jupyter Notebook (.ipynb)to the Canvas submission page.
Your notebook must includeanswers to both coding and discussion questions(all parts) in the
same file.
Your notebook must befully executable top-to-bottom(no missing cells, no hidden steps).
Includeclear markdown explanationsandwell-commented code.
You may discuss concepts with classmates, butall code and writing must be your own. List any
collaborators or resources you consulted.
Grading Notes
Partial credit is awarded based on the correctness, clarity, and completeness of your implementation
and discussion.
Your numerical results must match your discussion. Claims not supported by metrics will
receive reduced credit.
Your notebook must includetrain and test metricsfor every model you build.
Academic Integrity
All submissions must comply with the UW Student Conduct Code and the course academic integrity policy
posted on Canvas.
Part 1 (20 points): Fuel Consumption →Horsepower Prediction
Dataset:Fuel Consumption Based on HP (Kaggle)
Goal:Build regression models topredict horsepower (HP)based on fuel consumption features.
Required Models (all parts)

Linear Models:Linear Regression, Ridge Regression, Lasso Regression
Nonlinear Models (Polynomial):Degree 2 and Degree 3 only
Polynomial (deg=2) + Linear Regression
Polynomial (deg=3) + Linear Regression
Polynomial (deg=2) + Ridge Regression
Polynomial (deg=3) + Ridge Regression
Polynomial (deg=2) + Lasso Regression
Polynomial (deg=3) + Lasso Regression
Instructions
1.1 Load and inspect the dataset(5 points)

Load the CSV into a pandas DataFrame.
Display column names, shape, and summary statistics (describe()).
Identify missing values (if any) and clearly state how you handle them.
1.2 Train/Test split (70% / 30% random)(3 points)
Randomly split the dataset into70% trainingand30% testing.
Use a fixedrandomstatefor reproducibility.
1.3 Model training (Linear + Ridge + Lasso + Polynomial deg 2/3)(7 points)
Train all required models listed above to predictHP.
UsePolynomialFeatures+ a linear model (LinearRegression/Ridge/Lasso) for polynomial
models.
For Ridge/Lasso, you may tuneα(optional) but you must clearly report the chosen value(s).
1.4 Model evaluation (train and test)(3 points)
Foreach model, report metrics on bothtrainandtestsets:
MSE, MAE, R^2
Present your results in a clean table (recommended).
1.5 Discussion(2 points)
Using your reportedtrain and test metrics, explain:
Which model generalizes best (best test performance), and why do you think that
happens?
Part 2 (40 points): Weather→Daily Electricity Consumption Pre-
diction
Dataset:Electricity Consumption Based On Weather Data (Kaggle)
Goal:Build regression models topredict daily electricity consumptionusing weather features.
Instructions
2.1 Load and inspect the dataset(8 points)

Load the dataset into pandas.
Print column names, shape, summary statistics.
Clearly identify the dependent variable:dailyconsumption.
Identify missing values (if any) and handle them consistently.
2.2 Train/Test split (70% / 30% random)(5 points)
Randomly split into 70% training and 30% testing.
Use a fixedrandomstateso results are reproducible.
2.3 Model training (Linear + Ridge + Lasso + Polynomial deg 2/3)(15 points)
Train all required models (Linear/Ridge/Lasso and Polynomial deg 2/3 with Linear/Ridge/Lasso).
Ensure your features are correctly separated from the target.
You may tuneα(optional), but you must clearly report chosen value(s).
2.4 Model evaluation (train and test)(7 points)
For each model, report:
MSE, MAE, R^2
on both training and testing sets.
Present results in a well-formatted table.
2.5 Discussion(5 points)
Using your reportedtrain and test metrics, explain:
Which model generalizes best, and what does that suggest about whether electricity
consumption depends on weather linearly or nonlinearly?
Part 3 (40 points): Power Plant Data→ PE Prediction
Dataset:Power Plant Data (Kaggle)
Goal:Build regression models topredict electrical energy outputusing power-plant conditions.
Variables in the dataset

Independent Variables (IVs / Features):
AT:Ambient Temperature(the air temperature around the plant)
V:Exhaust Vacuum(vacuum level measured at the steam turbine exhaust)
AP:Ambient Pressure(the atmospheric air pressure around the plant)
RH:Relative Humidity(the amount of moisture in the air as a percentage)
Dependent Variable (DV / Target):
PE:Electrical Energy Output(power/energy output produced by the plant; target to predict)
Instructions
3.1 Load and inspect the dataset(8 points)

Load the dataset into pandas.
Print column names, shape, and summary statistics.
Clearly identify:
Target (DV):PE(Electrical Energy Output)
Features (IVs):AT(Ambient Temperature),V(Exhaust Vacuum),AP(Ambient Pressure),
RH(Relative Humidity)
Identify missing values (if any) and handle them consistently.
3.2 Train/Test split (70% / 30% random)(5 points)
Randomly split into 70% training and 30% testing.
Use a fixedrandomstateso results are reproducible.
3.3 Model training (Linear + Ridge + Lasso + Polynomial deg 2/3)(15 points)
Train all required models (Linear/Ridge/Lasso and Polynomial deg 2/3 with Linear/Ridge/Lasso).
UsePolynomialFeatures+ linear model (LinearRegression/Ridge/Lasso) for poly. models.
You may tuneα(optional), but you must clearly report chosen value(s).
3.4 Model evaluation (train and test)(7 points)
For each model, report:
MSE, MAE, R^2
on both training and testing sets.
Present results in a well-formatted table.
3.5 Discussion(5 points)
Using your reportedtrain and test metrics, explain:
Which model generalizes best for predicting PE, and why do you think Ridge/Lasso
helps (or does not help) on this dataset?
Recommended Results Table Format (for all parts)
You are encouraged to include a table similar to the following format in your notebook:

Table 1: Model performance summary (example format).
Model Train MSE Train MAE TrainR^2 Test MSE Test MAE TestR^2
Linear Regression
Ridge Regression
Lasso Regression
Poly2 + Linear
Poly3 + Linear
Poly2 + Ridge
Poly3 + Ridge
Poly2 + Lasso
Poly3 + Lasso
Final Reminder: Your discussion must be consistent with the evidence in your table(s). If you claim a
model is better, support it using test metrics(not training metrics).

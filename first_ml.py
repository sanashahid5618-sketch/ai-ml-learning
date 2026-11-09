import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Practice data: in examples se model seekhega
training_data = pd.DataFrame({
    "study_hours": [1, 2, 3],
    "marks": [40, 50, 60]
})

X_train = training_data[["study_hours"]]
y_train = training_data["marks"]

model = LinearRegression()
model.fit(X_train, y_train)

X_test = pd.DataFrame({"study_hours": [4, 5]})
actual_marks = [67, 85]
predicted_marks = model.predict(X_test)

average_marks = y_train.mean()
baseline_predictions = [average_marks, average_marks]

model_mae = mean_absolute_error(actual_marks, predicted_marks)
baseline_mae = mean_absolute_error(actual_marks, baseline_predictions)

print("=== Marks aur Predictions ===")
print("Actual marks:", actual_marks)
print("Model predictions:", predicted_marks.round(1))
print("Baseline predictions:", baseline_predictions)

print()
print("=== Error Comparison ===")
print("Model MAE:", round(model_mae, 1), "marks")
print("Baseline MAE:", round(baseline_mae, 1), "marks")
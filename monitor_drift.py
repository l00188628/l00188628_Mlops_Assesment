import pandas as pd

# Load original training data
original = pd.DataFrame({
    'age': [21, 25, 30, 35, 40]
})

# Load new data (simulate input drift)
new = pd.read_csv('new_input.csv')

# Compare means
original_mean = original['age'].mean()
new_mean = new['age'].mean()

print(f"Original Mean Age: {original_mean}")
print(f"New Mean Age: {new_mean}")

# Simple threshold-based drift detection
threshold = 5
if abs(original_mean - new_mean) > threshold:
    print("⚠️  Drift detected: consider retraining.")
else:
    print("✅ No significant drift detected.")
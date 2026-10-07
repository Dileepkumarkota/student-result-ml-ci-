import json
import sys


MIN_ACCURACY = 0.90

with open("metrics.json", "r") as file:
    metrics = json.load(file)

accuracy = float(metrics["accuracy"])

print(f"Model accuracy: {accuracy:.4f}")
print(f"Required minimum accuracy: {MIN_ACCURACY:.2f}")

if not 0.0 <= accuracy <= 1.0:
    print("QUALITY GATE FAILED: accuracy is outside the valid range.")
    sys.exit(1)

if accuracy < MIN_ACCURACY:
    print("QUALITY GATE FAILED: accuracy is below the required threshold.")
    sys.exit(1)

print("QUALITY GATE PASSED")

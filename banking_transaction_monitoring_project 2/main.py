
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("transactions.csv")

print("\nAll Transactions")
print(df.head())

# Detect suspicious transactions
suspicious = df[df["amount"] > 15000]

print("\nSuspicious Transactions (amount > 15000)")
print(suspicious)

# Basic statistics
print("\nAverage Transaction:", df["amount"].mean())
print("Highest Transaction:", df["amount"].max())
print("Lowest Transaction:", df["amount"].min())

# Visualization
plt.hist(df["amount"], bins=10)
plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.show()

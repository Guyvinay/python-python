import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Display the first few rows
print("First 5 rows of the dataset:\n", df.head())

# Overview of the dataset's structure
print("\nDataset info:\n", df.info())

# Check for missing values
print("\nMissing values per column:\n", df.isnull().sum())

# Get basic statistics on numerical columns
print("\nBasic statistics:\n", df.describe())



# Calculate mean age of passengers
mean_age = df['Age'].mean()
print("\nMean age of passengers:", mean_age)

# Calculate median age
median_age = df['Age'].median()
print("Median age of passengers:", median_age)

# Calculate standard deviation of age
std_dev_age = df['Age'].std()
print("Standard deviation of age:", std_dev_age)

# Probability of survival
total_passengers = len(df)
survived_passengers = len(df[df['Survived'] == 1])
p_survived = survived_passengers / total_passengers
print("\nTotal passenger: ", total_passengers, "\nTotal survived passengers: ", survived_passengers)
print("\nProbability of survival (P(Survived)):", p_survived)

# Probability of survival given that the passenger is female
female_passengers = df[df['Sex'] == 'female']
p_survived_given_female = len(female_passengers[female_passengers['Survived'] == 1]) / len(female_passengers)
print("Probability of survival given female (P(Survived | Female)):", p_survived_given_female)


# Plot distribution of ages
plt.figure(figsize=(10, 5))
plt.hist(df['Age'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Box plot to detect outliers in Fare
plt.figure(figsize=(10, 5))
plt.boxplot(df['Fare'].dropna())
plt.title("Box Plot of Passenger Fares")
plt.ylabel("Fare ($)")
plt.show()

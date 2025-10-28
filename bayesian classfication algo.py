# Bayesian Algo
# Naive Bayes PlayTennis Classifier in Python

# Training dataset
data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"]
]

# Count total Yes and No
totalYes = sum(1 for row in data if row[4] == "Yes")
totalNo = sum(1 for row in data if row[4] == "No")

# Calculate P(attribute=value | class)
def calc_likelihood(col, value, target):
    count_attr = sum(1 for row in data if row[4] == target and row[col] == value)
    count_class = sum(1 for row in data if row[4] == target)
    if count_class == 0:
        return 0
    return count_attr / count_class

# Naive Bayes Prediction
def predict(outlook, temp, humidity, wind):
    pYes = totalYes / len(data)
    pNo = totalNo / len(data)

    # Likelihoods for Yes
    yesLikelihood = (
        calc_likelihood(0, outlook, "Yes") *
        calc_likelihood(1, temp, "Yes") *
        calc_likelihood(2, humidity, "Yes") *
        calc_likelihood(3, wind, "Yes") *
        pYes
    )

    # Likelihoods for No
    noLikelihood = (
        calc_likelihood(0, outlook, "No") *
        calc_likelihood(1, temp, "No") *
        calc_likelihood(2, humidity, "No") *
        calc_likelihood(3, wind, "No") *
        pNo
    )

    return "Yes" if yesLikelihood > noLikelihood else "No"

# ---- Main Program ----
def main():
    print("Enter Outlook (Sunny/Overcast/Rain): ")
    outlook = input().strip()
    print("Enter Temperature (Hot/Mild/Cool): ")
    temp = input().strip()
    print("Enter Humidity (High/Normal): ")
    humidity = input().strip()
    print("Enter Wind (Weak/Strong): ")
    wind = input().strip()

    result = predict(outlook, temp, humidity, wind)
    print(f"Prediction: Will Play? -> {result}")

if __name__ == "__main__":
    main()
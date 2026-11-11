import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = sns.load_dataset("flights")

# Keep only the rows for 1960
data_1960 = data[data["year"] == 1960]

# Draw a line with a dot for each month
plt.figure(figsize=(8, 4))
plt.plot(data_1960["month"], data_1960["passengers"], marker="o")

# Add a title and labels
plt.title("Monthly Airline Passengers in 1960")
plt.xlabel("Month")
plt.ylabel("Passengers (thousands)")

# Fit everything neatly, save an image, and display the graph
plt.tight_layout()
plt.savefig("line_plot.png")
plt.show()


# Scatter plot using all years in the dataset
plt.figure(figsize=(8, 4))
plt.scatter(data["year"], data["passengers"], color="teal", alpha=0.7)

plt.title("Monthly Airline Passengers by Year")
plt.xlabel("Year")
plt.ylabel("Passengers (thousands)")

plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()

# Histogram of monthly passenger totals
plt.figure(figsize=(8, 4))
sns.histplot(data=data, x="passengers", bins=10, color="purple")

plt.title("Distribution of Monthly Airline Passengers")
plt.xlabel("Passengers per month (thousands)")
plt.ylabel("Number of months")

plt.tight_layout()
plt.savefig("histogram.png")
plt.show()

# Box plots comparing monthly passenger counts across years
plt.figure(figsize=(10, 5))
sns.boxplot(data=data, x="year", y="passengers", color="skyblue")

plt.title("Monthly Passenger Counts Across Years")
plt.xlabel("Year")
plt.ylabel("Passengers per month (thousands)")

plt.tight_layout()
plt.savefig("box_plot.png")
plt.show()
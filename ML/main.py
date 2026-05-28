import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("IPL_Sample_Data.csv")
print(data.head())

average_runs = data["Runs"].mean()
print("Average Runs:", average_runs)

wins = data[data["Result"] == "Win"]
print(wins)

print("Total Wins:", len(wins))

highest_runs = data["Runs"].max()
print("Highest Runs:", highest_runs)

team_runs = data.groupby("Team")["Runs"].mean()
print(team_runs)

team_runs.plot(kind="bar")

plt.title("Average Runs by Team")
plt.xlabel("Teams")
plt.ylabel("Average Runs")

plt.show()
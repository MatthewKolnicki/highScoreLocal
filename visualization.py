# import nba_high_scoring_games_2000_2024.csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("data/nba_game_logs_2000_2024.csv")
df = df[df["PTS"] >= 40]
# Create a box plot to show distribution of points by team
plt.figure(figsize=(15, 8))
sns.boxplot(data=df, x="HOME_TEAM", y="PTS", width=0.7)

# Add individual points on top of boxplot for better visibility
# sns.swarmplot(data=df, x='HOME_TEAM', y='PTS', color='red', size=4, alpha=0.5)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right")

# Add title and labels
plt.title("Distribution of 50+ Point Games by Location")
plt.xlabel("Home Team")
plt.ylabel("Points Scored")

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Display the plot
plt.show()

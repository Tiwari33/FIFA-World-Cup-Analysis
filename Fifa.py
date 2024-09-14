import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
world_cups = pd.read_csv(r"C:\Users\Nitesh Tiwari\Downloads\WorldCups.csv")
matches = pd.read_csv(r"C:\Users\Nitesh Tiwari\Downloads\WorldCupMatches.csv")
players = pd.read_csv(r"C:\Users\Nitesh Tiwari\Downloads\WorldCupPlayers.csv")
print(world_cups.isnull().sum())
print(players.isnull().sum())
print(matches.isnull().sum())
print(world_cups.describe())
print(players.describe())
print(matches.describe())
print(world_cups.columns)
print(players.columns)
print(matches.columns)
world_cups = world_cups.dropna()
players = players.fillna('Unknown')
matches = matches.dropna()
winners = world_cups[['Year', 'Winner']]
print(winners.head())

plt.figure(figsize=(12, 8))
sns.countplot(data=winners, x='Winner', order=winners['Winner'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Number of Wins by Each Country')
plt.subplot(2,2,1)
plt.show()
matches.columns = matches.columns.str.strip()
print(matches.columns)

matches['TotalGoals'] = matches["Home Team Goals"] + matches["Away Team Goals"]

plt.figure(figsize=(12, 8))
sns.histplot(matches['TotalGoals'], bins=range(0, 10), kde=True)
plt.title('Distribution of Total Goals per Match')
plt.xlabel('Total Goals')
plt.ylabel('Frequency')
plt.subplot(2,2,2)
plt.show()
top_scorers = players[['PlayerName', 'Goals']].sort_values(by='Goals', ascending=False).head(10)
print(top_scorers)

plt.figure(figsize=(12, 8))
sns.barplot(data=top_scorers, x='PlayerName', y='Goals', palette='viridis')
plt.xticks(rotation=90)
plt.title('Top 10 Goal Scorers')
plt.subplot(2,2,3)
plt.show()
team_performance = matches[['Year', 'HomeTeam', 'HomeGoals', 'AwayTeam', 'AwayGoals']]
team_performance['HomeWin'] = team_performance['HomeGoals'] > team_performance['AwayGoals']
team_performance['AwayWin'] = team_performance['HomeGoals'] < team_performance['AwayGoals']

yearly_wins = team_performance.groupby('Year').agg({'HomeWin': 'sum', 'AwayWin': 'sum'}).reset_index()

plt.figure(figsize=(12, 8))
sns.lineplot(data=yearly_wins, x='Year', y='HomeWin', label='Home Wins')
sns.lineplot(data=yearly_wins, x='Year', y='AwayWin', label='Away Wins')
plt.title('Home and Away Wins Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Wins')
plt.legend()
plt.subplot(2,2,4)
plt.show()

# get stats from nba_api
import nba_api
import pandas as pd
from nba_api.stats.library.data import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import cumestatsplayer
from nba_api.stats.endpoints import leaguegamelog


def get_game_logs():
    # 2000-2024
    seasons = [str(year) for year in range(2000, 2025)]
    game_logs = pd.DataFrame()
    for season in seasons:
        game_logs = pd.concat(
            [
                game_logs,
                leaguegamelog.LeagueGameLog(
                    player_or_team_abbreviation="P",
                    season=season,
                ).get_data_frames()[0],
            ]
        )
    game_logs["HOME_TEAM"] = game_logs.apply(get_home_team, axis=1)
    return game_logs


def high_scoring_games(game_logs, min_points=25):
    return game_logs[game_logs["PTS"] >= min_points]


# Function to extract home team from MATCHUP
def get_home_team(row):
    if " vs. " in row["MATCHUP"]:
        return row["TEAM_ABBREVIATION"]
    else:
        return row["MATCHUP"].split(" @ ")[1]


if __name__ == "__main__":
    game_logs = get_game_logs()
    high_scoring_game_logs = high_scoring_games(game_logs, min_points=25)
    game_logs.to_csv("data/nba_game_logs_2000_2024.csv", index=False)
    high_scoring_game_logs.to_csv(
        "data/nba_high_scoring_games_2000_2024.csv", index=False
    )

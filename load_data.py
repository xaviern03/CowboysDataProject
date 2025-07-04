import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:lola@localhost:54958/cowboys')

games = pd.read_csv('clean_data/clean_games.csv')
plays = pd.read_csv('clean_data/clean_plays.csv')
offense = pd.read_csv('clean_data/clean_offense.csv')
defense = pd.read_csv('clean_data/clean_defense.csv')

def filter_fk(child, parent, column):
    for fk in column:
        if fk not in child.columns or fk not in parent.columns:
            continue
        valid_key = set(parent[fk].dropna().unique())
        before = len(child)
        child = child[child[fk].isin(valid_key)]
        after = len(child)
    return child

plays = filter_fk(plays, games, ['game_id'])
defense = filter_fk(defense, plays, ['game_id', 'play_id'])
offense = filter_fk(offense, plays, ['game_id', 'play_id'])
offense = offense[offense['vs_player_play_id'].isin(defense['player_play_id'])]



try:
    games.to_sql('games', engine, if_exists='append', index=False)
    plays.to_sql('plays', engine, if_exists='append', index=False)
    defense.to_sql('defense', engine, if_exists='append', index=False)
    offense.to_sql('offense', engine, if_exists='append', index=False)
    print("** DONE **")
except Exception as e:
    print("Error during data load:", e)


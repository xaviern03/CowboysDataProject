import pandas as pd
import os
from cleaning import *
from config import *

def clean_data(filename, side):
    df = pd.read_csv(f"{filename}.csv")

    if 'player_play_id' in df.columns:
        df = remove_duplicate_ids(df, 'player_play_id')
    df = convert_bool_columns(df, BOOLEAN_COLUMNS.get(side, []))
    df = convert_to_null(df)
    df = upper_case_columns(df, UPPER_COLUMNS.get(side, []))
    df = lower_case_columns(df, LOWER_COLUMNS.get(side, []))
    df = numeric_bounds(df, NUMERIC_BOUNDS.get(side, {}))

    os.makedirs("clean_data", exist_ok=True)
    output_path = f"clean_data/clean_{filename}.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned file to {output_path}\n")


if __name__ == "__main__":
    clean_data('offense', 'offense')
    clean_data('defense', 'defense')
    clean_data('plays', 'plays')
    clean_data('games', 'games')

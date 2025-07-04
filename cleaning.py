def remove_duplicate_ids(df, id_column):
    df.drop_duplicates(subset=id_column, keep='first', inplace=True)
    return df

def convert_bool_columns(df, columns):
    for column in columns:
        if column in df.columns:
            df[column] = df[column].astype(str).str.strip().str.upper().map({
                "TRUE": True, "1": True,
                "FALSE": False, "0": False
            }).fillna(False)
    return df
    

def convert_to_null(df):
    df.replace('NA', None)
    return df

def upper_case_columns(df, columns):
    for column in columns:
        if column in df.columns and df[column].dtype == 'object':
            df[column] = df[column].str.upper()
    return df    

def lower_case_columns(df, columns):
    for column in columns:
        if column in df.columns and df[column].dtype == 'object':
            df[column] = df[column].str.lower()
    return df

def numeric_bounds(df, column_bounds):
    for column, (lower, upper) in column_bounds.items():
        if column in df.columns:
            out_of_bounds = df[(df[column] < lower) | (df[column] > upper)]
            if not out_of_bounds.empty:
                print(f"Out of bounds in column '{column}':")
                for index, row in out_of_bounds.iterrows():
                    print(f"Row {index}: {row[column]} (expected between {lower} and {upper})")
            else:
                print(f"No out of bounds values in column '{column}'.")

    return df


import pandas as pd


def load_data(file):
    """
    Reads CSV safely from Streamlit upload OR file path
    """

    try:
        df = pd.read_csv(file, encoding='utf-8')
    except:
        df = pd.read_csv(file, encoding='latin1')

    df.columns = df.columns.str.strip().str.lower()
    return df


def clean_data(df):
    """
    Converts ANY variant of dataset into standard schema:
    date | value | country
    """

    df.columns = df.columns.str.strip().str.lower()

    # -------- DATE HANDLING --------
    if 'dt' in df.columns:
        df['date'] = pd.to_datetime(df['dt'], errors='coerce')
    elif 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    else:
        raise ValueError(f"No date column found. Columns: {df.columns.tolist()}")

    # -------- VALUE HANDLING --------
    temp_cols = ['averagetemperature', 'temperature', 'temp']
    value_col = None

    for col in temp_cols:
        if col in df.columns:
            value_col = col
            break

    if value_col is None:
        raise ValueError(f"No temperature column found. Columns: {df.columns.tolist()}")

    df['value'] = pd.to_numeric(df[value_col], errors='coerce')

    # -------- COUNTRY HANDLING --------
    if 'country' not in df.columns:
        df['country'] = "Unknown"
    else:
        df['country'] = df['country'].fillna("Unknown")

    # CLEAN
    df = df.dropna(subset=['date', 'value'])

    return df


def add_time_features(df):

    df = df.sort_values('date')

    df['moving_avg'] = df['value'].rolling(7, min_periods=1).mean()
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month

    return df


def preprocess(file):
    df = load_data(file)
    df = clean_data(df)
    df = add_time_features(df)

    return df
import numpy as np
import pandas as pd

# ✅ Method 1: Z-score based anomaly detection
def detect_anomalies_zscore(df):
    mean = df['temp'].mean()
    std = df['temp'].std()

    df['z_score'] = (df['temp'] - mean) / std

    df['anomaly_zscore'] = np.where(
        (df['z_score'] > 2) | (df['z_score'] < -2),
        1, 0
    )

    return df


# ✅ Method 2: Rolling (Time-Series aware) anomaly detection
def detect_anomalies_rolling(df, window=12):
    df = df.sort_values('date')

    rolling_mean = df['temp'].rolling(window=window).mean()
    rolling_std = df['temp'].rolling(window=window).std()

    df['rolling_mean'] = rolling_mean
    df['rolling_std'] = rolling_std

    df['anomaly_rolling'] = np.where(
        (df['temp'] > rolling_mean + 2 * rolling_std) |
        (df['temp'] < rolling_mean - 2 * rolling_std),
        1, 0
    )

    return df


# ✅ Combine both methods (BEST PRACTICE)
def detect_anomalies(df):
    df = detect_anomalies_zscore(df)
    df = detect_anomalies_rolling(df)

    # Final anomaly flag (if either detects anomaly)
    df['anomaly'] = np.where(
        (df['anomaly_zscore'] == 1) | (df['anomaly_rolling'] == 1),
        1, 0
    )

    return df
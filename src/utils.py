import matplotlib.pyplot as plt


def plot_line(df):

    plt.figure(figsize=(10, 5))

    plt.plot(df['date'], df['value'], label='Temperature', alpha=0.5)
    plt.plot(df['date'], df['moving_avg'], label='Moving Avg')

    plt.legend()
    plt.title("Climate Trend")
    plt.xlabel("Date")
    plt.ylabel("Value")

    return plt


def plot_bar(df):

    yearly = df.groupby('year')['value'].mean()

    plt.figure(figsize=(10, 5))
    plt.bar(yearly.index, yearly.values)

    plt.title("Yearly Trend")

    return plt


def plot_pie(df):

    counts = df['country'].value_counts().head(10)

    plt.figure(figsize=(6, 6))
    plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')

    return plt
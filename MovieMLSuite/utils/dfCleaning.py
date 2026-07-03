def Cleaning(df):
    df = df.dropna()

    cols = ["Movie", "Director", "Running time", "Genre", "Release year"]
    df = df.drop_duplicates(subset=cols, keep="last")

    df = df.reset_index(drop=True)

    return df
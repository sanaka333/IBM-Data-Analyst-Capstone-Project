import pandas as pd

df = pd.read_csv("survey_data_updated.csv")


top10_languages = (
    df['LanguageHaveWorkedWith']
    .str.split(";")
    .explode()
    .value_counts()
    .head(10)
    .reset_index()
)

top10_languages.columns = ['Language', 'Count']

top10_databases = (
    df['DatabaseHaveWorkedWith']
    .str.split(";")
    .explode()
    .value_counts()
    .head(10)
    .reset_index()
)

top10_databases.columns = ['Database', 'Count']

top10_platforms = (
    df['PlatformHaveWorkedWith']
    .str.split(";")
    .explode()
    .value_counts()
    .head(10)
    .reset_index()
)

top10_platforms.columns = ['Platform', 'Count']

top10_webframes = (
    df['WebframeHaveWorkedWith']
    .str.split(";")
    .explode()
    .value_counts()
    .head(10)
    .reset_index()
)

top10_webframes.columns = ['Webframe', 'Count']

top10_languages.to_csv("top10_languages.csv", index=False)
top10_databases.to_csv("top10_databases.csv", index=False)
top10_platforms.to_csv("top10_platforms.csv", index=False)
top10_webframes.to_csv("top10_webframes.csv", index=False)



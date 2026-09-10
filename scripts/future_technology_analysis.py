import pandas as pd

df = pd.read_csv("survey_data_updated.csv")

top10_languages_in_future = (
    df['LanguageWantToWorkWith']
    .str.split(";")
    .explode()
    .value_counts()
    .head(10)
    .reset_index()
)

top10_languages_in_future.columns = ['Language', 'Count']

top10_databases_in_future = (
    df['DatabaseWantToWorkWith']
    .str.split(";")
    .explode()
    .value_counts()
    .head(10)
    .reset_index()
)

top10_databases_in_future.columns = ['Database', 'Count']

top10_platforms_in_future = (
    df['PlatformWantToWorkWith']
    .str.split(";")
    .explode()
    .value_counts()
    .head(10)
    .reset_index()
)

top10_platforms_in_future.columns = ['Platform', 'Count']

top10_webframes_in_future = (
    df['WebframeWantToWorkWith']
    .str.split(";")
    .explode()
    .value_counts()
    .head(10)
    .reset_index()
)

top10_webframes_in_future.columns = ['Webframe', 'Count']

top10_languages_in_future.to_csv("top10_languages_in_future.csv", index=False)
top10_databases_in_future.to_csv("top10_databases_in_future.csv", index=False)
top10_platforms_in_future.to_csv("top10_platforms_in_future.csv", index=False)
top10_webframes_in_future.to_csv("top10_webframes_in_future.csv", index=False)



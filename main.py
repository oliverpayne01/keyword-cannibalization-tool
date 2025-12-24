import pandas as pd

csv_path = "/Users/oliver.payne/Desktop/keywords.csv"
df_raw = pd.read_csv(csv_path)

df_grouped = (
    df_raw.groupby("Keyword")["URL"].agg(lambda x: ", ".join(sorted(set(x)))).reset_index()
)

df_grouped["url_count"] = df_grouped["URL"].apply(lambda x: len(x.split(", ")))
df_rows_to_remove = df_grouped[df_grouped["url_count"] == 1].index
df_filtered = df_grouped.drop(df_rows_to_remove)

df_filtered.to_csv("output.csv")

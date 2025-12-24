import pandas as pd

csv_path = "/Users/oliver.payne/Desktop/keywords.csv"
df = pd.read_csv(csv_path)

grouped = (
    df.groupby("Keyword")["URL"].agg(lambda x: ", ".join(sorted(set(x)))).reset_index()
)

grouped["url_count"] = grouped["URL"].apply(lambda x: len(x.split(", ")))

grouped.to_csv("output.csv")

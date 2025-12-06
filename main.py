import pandas as pd
import re

csv_path = "/Users/oliver.payne/Desktop/Queries.csv"
df = pd.read_csv(csv_path)

def preprocess_data():
  def non_branded_rows():
    return df[~df["Top queries"].str.contains("colonial")]

  def rows_with_clicks():
    return non_branded_rows()[df["Clicks"] > 0]

  return rows_with_clicks()

df = preprocess_data()
print (df)

# Identify cannibalization
# Create a list of cannibalization candidates
# Calculate clicks per query / click share etc.
# Print results

import pandas as pd
import sys

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())
print("arguments", sys.argv)

month = int(sys.argv[1])

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

print(f'hello pipeline, month={month}')
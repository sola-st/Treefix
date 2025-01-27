# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 3867
path = datapath("io", "json", "data", "teams.csv")
df = pd.read_csv(path)
s = df.to_json()
result = read_json(s)
tm.assert_frame_equal(result.reindex(index=df.index, columns=df.columns), df)

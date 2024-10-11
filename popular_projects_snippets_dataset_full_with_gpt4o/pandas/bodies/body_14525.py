# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py
# GH 33878
df = pd.DataFrame({"A": [1, 2], "B": ["x", "y"], "C": [True, False]})
expected = df[["B", "A"]]
self.check_round_trip(df, expected, columns=["B", "A"])

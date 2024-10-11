# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
# gh-11637: incorrect output when a mix of integer and string column
# names passed as columns parameter in to_csv

df = DataFrame({0: ["a", "b", "c"], 1: ["aa", "bb", "cc"]})
df["test"] = "txt"
assert df.to_csv() == df.to_csv(columns=[0, 1, "test"])

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_pop.py
df = DataFrame({0: [0, 1], 1: [0, 1], 2: [4, 5]})
df.columns = ["a", "b", "a"]

res = df.pop("a")
assert type(res) == DataFrame
assert len(res) == 2
assert len(df.columns) == 1
assert "b" in df.columns
assert "a" not in df.columns
assert len(df.index) == 2

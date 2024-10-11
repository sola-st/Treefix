# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# GH 16923
d = {"A": ["B", "E", "C", "A", "E"]}
df = DataFrame(data=d)
df["A"] = df["A"].astype("category")
with tm.ensure_clean() as path:
    df.to_stata(path, write_index=write_index)

    with read_stata(path, iterator=True) as dta_iter:
        value_labels = dta_iter.value_labels()
assert value_labels == {"A": {0: "A", 1: "B", 2: "C", 3: "E"}}

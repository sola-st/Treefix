# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
data = {
    "title": ["foobar", "bar", "foobar"] + ["foobar"] * 17,
    "cruft": np.random.random(20),
}

df = DataFrame(data)
ix = df[df["title"] == "bar"].index

df.loc[ix, ["title"]] = "foobar"
df.loc[ix, ["cruft"]] = 0

assert df.loc[1, "title"] == "foobar"
assert df.loc[1, "cruft"] == 0

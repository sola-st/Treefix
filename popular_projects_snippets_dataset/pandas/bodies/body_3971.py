# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
# DataFrame whose columns are identifiers shall have them in __dir__.
df = DataFrame([list("abcd"), list("efgh")], columns=list("ABCD"))
for key in list("ABCD"):
    assert key in dir(df)
assert isinstance(df.__getitem__("A"), Series)

# DataFrame whose first-level columns are identifiers shall have
# them in __dir__.
df = DataFrame(
    [list("abcd"), list("efgh")],
    columns=pd.MultiIndex.from_tuples(list(zip("ABCD", "EFGH"))),
)
for key in list("ABCD"):
    assert key in dir(df)
for key in list("EFGH"):
    assert key not in dir(df)
assert isinstance(df.__getitem__("A"), DataFrame)

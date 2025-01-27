# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_integrity.py
# GH 18165
r = list(range(1000000))
df = pd.DataFrame(
    {"a": r, "b": r}, index=MultiIndex.from_tuples([(x, x) for x in r])
)

msg = "'Series' object has no attribute 'foo'"
with pytest.raises(AttributeError, match=msg):
    df["a"].foo()

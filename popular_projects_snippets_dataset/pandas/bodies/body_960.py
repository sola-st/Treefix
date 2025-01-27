# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval.py
# CategoricalIndex with IntervalIndex categories
df = DataFrame({"A": range(10)})
ser = pd.cut(df.A, 5)
df["B"] = ser
df = df.set_index("B")

result = df.loc[4]
expected = df.iloc[4:6]
tm.assert_frame_equal(result, expected)

with pytest.raises(KeyError, match="10"):
    df.loc[10]

# single list-like
result = df.loc[[4]]
expected = df.iloc[4:6]
tm.assert_frame_equal(result, expected)

# non-unique
result = df.loc[[4, 5]]
expected = df.take([4, 5, 4, 5])
tm.assert_frame_equal(result, expected)

with pytest.raises(KeyError, match=r"None of \[\[10\]\] are"):
    df.loc[[10]]

# partial missing
with pytest.raises(KeyError, match=r"\[10\] not in index"):
    df.loc[[10, 4]]

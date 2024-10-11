# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_equals.py
# Add object dtype column with nans
index = np.random.random(10)
df1 = DataFrame(np.random.random(10), index=index, columns=["floats"])
df1["text"] = "the sky is so blue. we could use more chocolate.".split()
df1["start"] = date_range("2000-1-1", periods=10, freq="T")
df1["end"] = date_range("2000-1-1", periods=10, freq="D")
df1["diff"] = df1["end"] - df1["start"]
# Explicitly cast to object, to avoid implicit cast when setting np.nan
df1["bool"] = (np.arange(10) % 3 == 0).astype(object)
df1.loc[::2] = np.nan
df2 = df1.copy()
assert df1["text"].equals(df2["text"])
assert df1["start"].equals(df2["start"])
assert df1["end"].equals(df2["end"])
assert df1["diff"].equals(df2["diff"])
assert df1["bool"].equals(df2["bool"])
assert df1.equals(df2)
assert not df1.equals(object)

# different dtype
different = df1.copy()
different["floats"] = different["floats"].astype("float32")
assert not df1.equals(different)

# different index
different_index = -index
different = df2.set_index(different_index)
assert not df1.equals(different)

# different columns
different = df2.copy()
different.columns = df2.columns[::-1]
assert not df1.equals(different)

# DatetimeIndex
index = date_range("2000-1-1", periods=10, freq="T")
df1 = df1.set_index(index)
df2 = df1.copy()
assert df1.equals(df2)

# MultiIndex
df3 = df1.set_index(["text"], append=True)
df2 = df1.set_index(["text"], append=True)
assert df3.equals(df2)

df2 = df1.set_index(["floats"], append=True)
assert not df3.equals(df2)

# NaN in index
df3 = df1.set_index(["floats"], append=True)
df2 = df1.set_index(["floats"], append=True)
assert df3.equals(df2)

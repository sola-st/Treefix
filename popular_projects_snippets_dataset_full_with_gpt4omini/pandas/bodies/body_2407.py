# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# corner case
df = DataFrame({"B": [1.0, 2.0, 3.0], "C": ["a", "b", "c"]}, index=np.arange(3))
del df["B"]
df["B"] = [1.0, 2.0, 3.0]
assert "B" in df
assert len(df.columns) == 2

df["A"] = "beginning"
df["E"] = "foo"
df["D"] = "bar"
df[datetime.now()] = "date"
df[datetime.now()] = 5.0

# what to do when empty frame with index
dm = DataFrame(index=float_frame.index)
dm["A"] = "foo"
dm["B"] = "bar"
assert len(dm.columns) == 2
assert dm.values.dtype == np.object_

# upcast
dm["C"] = 1
assert dm["C"].dtype == np.int64

dm["E"] = 1.0
assert dm["E"].dtype == np.float64

# set existing column
dm["A"] = "bar"
assert "bar" == dm["A"][0]

dm = DataFrame(index=np.arange(3))
dm["A"] = 1
dm["foo"] = "bar"
del dm["foo"]
dm["foo"] = "bar"
assert dm["foo"].dtype == np.object_

dm["coercible"] = ["1", "2", "3"]
assert dm["coercible"].dtype == np.object_

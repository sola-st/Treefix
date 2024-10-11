# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_filter.py
# Items
filtered = float_frame.filter(["A", "B", "E"])
assert len(filtered.columns) == 2
assert "E" not in filtered

filtered = float_frame.filter(["A", "B", "E"], axis="columns")
assert len(filtered.columns) == 2
assert "E" not in filtered

# Other axis
idx = float_frame.index[0:4]
filtered = float_frame.filter(idx, axis="index")
expected = float_frame.reindex(index=idx)
tm.assert_frame_equal(filtered, expected)

# like
fcopy = float_frame.copy()
fcopy["AA"] = 1

filtered = fcopy.filter(like="A")
assert len(filtered.columns) == 2
assert "AA" in filtered

# like with ints in column names
df = DataFrame(0.0, index=[0, 1, 2], columns=[0, 1, "_A", "_B"])
filtered = df.filter(like="_")
assert len(filtered.columns) == 2

# regex with ints in column names
# from PR #10384
df = DataFrame(0.0, index=[0, 1, 2], columns=["A1", 1, "B", 2, "C"])
expected = DataFrame(
    0.0, index=[0, 1, 2], columns=pd.Index([1, 2], dtype=object)
)
filtered = df.filter(regex="^[0-9]+$")
tm.assert_frame_equal(filtered, expected)

expected = DataFrame(0.0, index=[0, 1, 2], columns=[0, "0", 1, "1"])
# shouldn't remove anything
filtered = expected.filter(regex="^[0-9]+$")
tm.assert_frame_equal(filtered, expected)

# pass in None
with pytest.raises(TypeError, match="Must pass"):
    float_frame.filter()
with pytest.raises(TypeError, match="Must pass"):
    float_frame.filter(items=None)
with pytest.raises(TypeError, match="Must pass"):
    float_frame.filter(axis=1)

# test mutually exclusive arguments
with pytest.raises(TypeError, match="mutually exclusive"):
    float_frame.filter(items=["one", "three"], regex="e$", like="bbi")
with pytest.raises(TypeError, match="mutually exclusive"):
    float_frame.filter(items=["one", "three"], regex="e$", axis=1)
with pytest.raises(TypeError, match="mutually exclusive"):
    float_frame.filter(items=["one", "three"], regex="e$")
with pytest.raises(TypeError, match="mutually exclusive"):
    float_frame.filter(items=["one", "three"], like="bbi", axis=0)
with pytest.raises(TypeError, match="mutually exclusive"):
    float_frame.filter(items=["one", "three"], like="bbi")

# objects
filtered = float_string_frame.filter(like="foo")
assert "foo" in filtered

# unicode columns, won't ascii-encode
df = float_frame.rename(columns={"B": "\u2202"})
filtered = df.filter(like="C")
assert "C" in filtered

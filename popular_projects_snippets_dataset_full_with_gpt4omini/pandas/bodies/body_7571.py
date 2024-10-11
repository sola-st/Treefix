# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_conversion.py
# GH 45245
data = [(1, 2), (3, 4)]
names = ["a", "a"]
index = MultiIndex.from_tuples(data, names=names)
with pytest.raises(ValueError, match="Cannot create duplicate column labels"):
    index.to_frame()

result = index.to_frame(allow_duplicates=True)
expected = DataFrame(data, index=index, columns=names)
tm.assert_frame_equal(result, expected)

names = [None, 0]
index = MultiIndex.from_tuples(data, names=names)
with pytest.raises(ValueError, match="Cannot create duplicate column labels"):
    index.to_frame()

result = index.to_frame(allow_duplicates=True)
expected = DataFrame(data, index=index, columns=[0, 0])
tm.assert_frame_equal(result, expected)

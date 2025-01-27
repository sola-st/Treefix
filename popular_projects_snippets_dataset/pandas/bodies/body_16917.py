# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_dataframe.py
# GH#42651
index = [1, 1, 3]
data = [1, 2, 3]

df = DataFrame(data=data, index=index)
result = concat([df], keys=["A"], names=["ID", "date"])
mi = pd.MultiIndex.from_product([["A"], index], names=["ID", "date"])
expected = DataFrame(data=data, index=mi)
tm.assert_frame_equal(result, expected)
tm.assert_index_equal(result.index.levels[1], Index([1, 3], name="date"))

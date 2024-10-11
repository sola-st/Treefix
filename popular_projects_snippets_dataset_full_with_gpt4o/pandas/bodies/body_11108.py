# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
deleveled = mframe.reset_index()

mapper0 = {"foo": 0, "bar": 0, "baz": 1, "qux": 1}
mapper1 = {"one": 0, "two": 0, "three": 1}

result0 = mframe.groupby(mapper0, level=0).sum()
result1 = mframe.groupby(mapper1, level=1).sum()

mapped_level0 = np.array(
    [mapper0.get(x) for x in deleveled["first"]], dtype=np.int64
)
mapped_level1 = np.array(
    [mapper1.get(x) for x in deleveled["second"]], dtype=np.int64
)
expected0 = mframe.groupby(mapped_level0).sum()
expected1 = mframe.groupby(mapped_level1).sum()
expected0.index.name, expected1.index.name = "first", "second"

tm.assert_frame_equal(result0, expected0)
tm.assert_frame_equal(result1, expected1)

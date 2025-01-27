# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH: 34832
expected = DataFrame({"idx": [1, 2, 3], "obj": Series([obj] * 3, dtype=dtype)})

df = DataFrame({"idx": [1, 2, 3]})
df["obj"] = obj

tm.assert_frame_equal(df, expected)

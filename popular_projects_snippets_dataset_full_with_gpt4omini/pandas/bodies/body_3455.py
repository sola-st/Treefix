# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# GH#36541: that reset_index() does not raise ValueError
ix = MultiIndex.from_tuples(ix_data, names=["a", "b"])
result = DataFrame({"x": [11, 12]}, index=ix)
result = result.reset_index()

expected = DataFrame(exp_data)
tm.assert_frame_equal(result, expected)

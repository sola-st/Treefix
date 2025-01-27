# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
ts0 = Series(np.zeros(5))
ts1 = Series(np.ones(5))
ts0.name = ts1.name = "same name"
result = concat([ts0, ts1], axis=1)

expected = DataFrame({0: ts0, 1: ts1})
expected.columns = ["same name", "same name"]
tm.assert_frame_equal(result, expected)

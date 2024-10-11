# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
df = DataFrame({0.0: np.random.rand(10), 1.0: np.random.rand(10)})
df["a"] = 10

expected = DataFrame({0.0: df[0.0], 1.0: df[1.0], "a": [10] * 10})
tm.assert_frame_equal(expected, df)

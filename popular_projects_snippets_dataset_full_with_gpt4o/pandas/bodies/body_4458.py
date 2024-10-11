# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
idx = Index(range(3))
df = DataFrame({"a": 0}, index=idx)
expected = DataFrame({"a": [0, 0, 0]}, index=idx)
tm.assert_frame_equal(df, expected, check_dtype=False)

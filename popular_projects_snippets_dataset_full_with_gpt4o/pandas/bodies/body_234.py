# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH#35683 get columns correct
df = DataFrame([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], columns=["a", "b"])

result = df.apply(lambda x: [], result_type="reduce")
expected = Series({"a": [], "b": []}, dtype=object)
tm.assert_series_equal(result, expected)

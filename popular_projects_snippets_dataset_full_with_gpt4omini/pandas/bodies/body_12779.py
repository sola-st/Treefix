# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH 21536
result = json_normalize({"A": [1, 2]}, "A", record_prefix="Prefix.")
expected = DataFrame([[1], [2]], columns=["Prefix.0"])
tm.assert_frame_equal(result, expected)

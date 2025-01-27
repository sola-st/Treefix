# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 25512
# format='%Y%m%d', errors='coerce'
result = to_datetime(input_s, format="%Y%m%d", errors="coerce")
tm.assert_series_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
result = df1.melt(id_vars, value_vars, col_level=col_level)
tm.assert_frame_equal(result, expected)

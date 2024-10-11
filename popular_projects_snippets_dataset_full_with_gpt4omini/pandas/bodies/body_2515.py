# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_get_value.py
for idx in float_frame.index:
    for col in float_frame.columns:
        result = float_frame._get_value(idx, col)
        expected = float_frame[col][idx]
        assert result == expected

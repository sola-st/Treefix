# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_set_value.py
for idx in float_frame.index:
    for col in float_frame.columns:
        float_frame._set_value(idx, col, 1)
        assert float_frame[col][idx] == 1

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_align.py

af, bf = float_string_frame.align(
    float_string_frame, join="inner", axis=1, method="pad"
)
tm.assert_index_equal(bf.columns, float_string_frame.columns)

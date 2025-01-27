# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 36113
result = (
    DataFrame(dtype=np.int64).stack(dropna=dropna).unstack(fill_value=fill_value)
)
expected = DataFrame(dtype=np.int64)
tm.assert_frame_equal(result, expected)

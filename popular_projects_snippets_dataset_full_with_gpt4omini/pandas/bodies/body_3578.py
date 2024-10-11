# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH 29687
expected = DataFrame(
    {"col1": [1, 2, 3], "col2": [3, 4, 5]},
    index=pd.date_range("2020", periods=3),
)
with pd.option_context("mode.use_inf_as_na", True):
    result = expected.sort_index()
tm.assert_frame_equal(result, expected)

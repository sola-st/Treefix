# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# check for regressions on this issue:
# https://github.com/pandas-dev/pandas/issues/19351
# make sure DataFrame.unstack() works when its run on a subset of the DataFrame
# and the Index levels contain values that are not present in the subset
result = DataFrame(result_rows, columns=result_columns).set_index(
    ["ix1", "ix2"]
)
result = result.iloc[1:2].unstack("ix2")
expected = DataFrame(
    [expected_row],
    columns=MultiIndex.from_product(
        [result_columns[2:], [index_product]], names=[None, "ix2"]
    ),
    index=Index([2], name="ix1"),
)
tm.assert_frame_equal(result, expected)

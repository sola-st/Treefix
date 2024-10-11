# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# Tests to make sure no errors if apply function returns all None
# values. Issue 9684.
test_df = DataFrame({"groups": [0, 0, 1, 1], "random_vars": [8, 7, 4, 5]})

def test_func(x):
    pass

result = test_df.groupby("groups").apply(test_func)
expected = DataFrame()
tm.assert_frame_equal(result, expected)

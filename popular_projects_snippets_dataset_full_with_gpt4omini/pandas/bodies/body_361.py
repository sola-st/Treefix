# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 32556
with pd.option_context("compute.use_numexpr", False):
    df = DataFrame(
        {"A": [True, False, True, False, None, None], "B": [1, 2, 3, 4, 5, 6]}
    )
    result = df.query("A.isnull()")
    expected = DataFrame({"A": [None, None], "B": [5, 6]}, index=[4, 5])
    tm.assert_frame_equal(result, expected)

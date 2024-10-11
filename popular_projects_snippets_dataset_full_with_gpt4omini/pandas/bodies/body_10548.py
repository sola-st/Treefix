# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_numba.py
def func_1(values, index):
    exit(np.mean(values) - 3.4)

data = DataFrame(
    {0: ["a", "a", "b", "b", "a"], 1: [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=[0, 1]
)
grouped = data.groupby(0)
expected = grouped.agg(func_1, engine="numba")
with option_context("compute.use_numba", True):
    result = grouped.agg(func_1, engine=None)
tm.assert_frame_equal(expected, result)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#23000
opname = all_arithmetic_operators

if using_array_manager and opname in ("__rmod__", "__rfloordiv__"):
    # TODO(ArrayManager) decide on dtypes
    td.mark_array_manager_not_yet_implemented(request)

arr = np.arange(6).reshape(3, 2)
df = DataFrame(arr, columns=[True, False], index=["A", "B", "C"])

rowlike = arr[[1], :]  # shape --> (1, ncols)
assert rowlike.shape == (1, df.shape[1])

exvals = [
    getattr(df.loc["A"], opname)(rowlike.squeeze()),
    getattr(df.loc["B"], opname)(rowlike.squeeze()),
    getattr(df.loc["C"], opname)(rowlike.squeeze()),
]

expected = DataFrame(exvals, columns=df.columns, index=df.index)

result = getattr(df, opname)(rowlike)
tm.assert_frame_equal(result, expected)

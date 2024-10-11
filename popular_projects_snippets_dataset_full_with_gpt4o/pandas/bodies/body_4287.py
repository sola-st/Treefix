# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#23000
opname = all_arithmetic_operators

if using_array_manager and opname in ("__rmod__", "__rfloordiv__"):
    # TODO(ArrayManager) decide on dtypes
    td.mark_array_manager_not_yet_implemented(request)

arr = np.arange(6).reshape(3, 2)
df = DataFrame(arr, columns=[True, False], index=["A", "B", "C"])

collike = arr[:, [1]]  # shape --> (nrows, 1)
assert collike.shape == (df.shape[0], 1)

exvals = {
    True: getattr(df[True], opname)(collike.squeeze()),
    False: getattr(df[False], opname)(collike.squeeze()),
}

dtype = None
if opname in ["__rmod__", "__rfloordiv__"]:
    # Series ops may return mixed int/float dtypes in cases where
    #   DataFrame op will return all-float.  So we upcast `expected`
    dtype = np.common_type(*(x.values for x in exvals.values()))

expected = DataFrame(exvals, columns=df.columns, index=df.index, dtype=dtype)

result = getattr(df, opname)(collike)
tm.assert_frame_equal(result, expected)

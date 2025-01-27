# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
# the dunder __pos__ works if and only if np.positive works,
#  same for __neg__/np.negative and __abs__/np.abs
attr = {np.positive: "__pos__", np.negative: "__neg__", np.abs: "__abs__"}[
    ufunc
]

exc = None
try:
    result = getattr(data, attr)()
except Exception as err:
    exc = err

    # if __pos__ raised, then so should the ufunc
    with pytest.raises((type(exc), TypeError)):
        ufunc(data)
else:
    alt = ufunc(data)
    self.assert_extension_array_equal(result, alt)

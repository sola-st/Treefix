# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        If necessary, squeeze a (N, 1) ndarray to (N,)
        """
# e.g. if we are passed a 2D mask for putmask
if (
    isinstance(arg, (np.ndarray, ExtensionArray))
    and arg.ndim == self.values.ndim + 1
):
    # TODO(EA2D): unnecessary with 2D EAs
    assert arg.shape[1] == 1
    # error: No overload variant of "__getitem__" of "ExtensionArray"
    # matches argument type "Tuple[slice, int]"
    arg = arg[:, 0]  # type: ignore[call-overload]
elif isinstance(arg, ABCDataFrame):
    # 2022-01-06 only reached for setitem
    # TODO: should we avoid getting here with DataFrame?
    assert arg.shape[1] == 1
    arg = arg._ixs(0, axis=1)._values

exit(arg)

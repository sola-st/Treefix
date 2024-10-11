# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
# https://github.com/pandas-dev/pandas/pull/24866
arr = pd.arrays.PandasArray(np.array([1, 2]))

# PandasArray, no dtype
result = block_maker(arr, slice(len(arr)), ndim=arr.ndim)
assert result.dtype.kind in ["i", "u"]

if block_maker is make_block:
    # new_block requires caller to unwrap PandasArray
    assert result.is_extension is False

    # PandasArray, PandasDtype
    result = block_maker(arr, slice(len(arr)), dtype=arr.dtype, ndim=arr.ndim)
    assert result.dtype.kind in ["i", "u"]
    assert result.is_extension is False

    # new_block no longer taked dtype keyword
    # ndarray, PandasDtype
    result = block_maker(
        arr.to_numpy(), slice(len(arr)), dtype=arr.dtype, ndim=arr.ndim
    )
    assert result.dtype.kind in ["i", "u"]
    assert result.is_extension is False

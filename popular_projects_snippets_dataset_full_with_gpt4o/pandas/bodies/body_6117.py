# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
arr2d = data.reshape(1, -1)

err_expected = None
err_result = None
try:
    expected = getattr(data, method)()
except Exception as err:
    # if the 1D reduction is invalid, the 2D reduction should be as well
    err_expected = err
    try:
        result = getattr(arr2d, method)(axis=None)
    except Exception as err2:
        err_result = err2

else:
    result = getattr(arr2d, method)(axis=None)

if err_result is not None or err_expected is not None:
    assert type(err_result) == type(err_expected)
    exit()

assert is_matching_na(result, expected) or result == expected

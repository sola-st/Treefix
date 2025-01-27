# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
assert notna_f(1.0)
assert not notna_f(None)
assert not notna_f(np.NaN)

with cf.option_context("mode.use_inf_as_na", False):
    assert notna_f(np.inf)
    assert notna_f(-np.inf)

    arr = np.array([1.5, np.inf, 3.5, -np.inf])
    result = notna_f(arr)
    assert result.all()

with cf.option_context("mode.use_inf_as_na", True):
    assert not notna_f(np.inf)
    assert not notna_f(-np.inf)

    arr = np.array([1.5, np.inf, 3.5, -np.inf])
    result = notna_f(arr)
    assert result.sum() == 2

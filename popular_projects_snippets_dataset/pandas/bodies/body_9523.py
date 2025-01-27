# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_reduction.py
# the methods return numpy scalars
exp_any = pd.NA if exp_any is pd.NA else np.bool_(exp_any)
exp_all = pd.NA if exp_all is pd.NA else np.bool_(exp_all)
exp_any_noskip = pd.NA if exp_any_noskip is pd.NA else np.bool_(exp_any_noskip)
exp_all_noskip = pd.NA if exp_all_noskip is pd.NA else np.bool_(exp_all_noskip)

for con in [pd.array, pd.Series]:
    a = con(values, dtype="boolean")
    assert a.any() is exp_any
    assert a.all() is exp_all
    assert a.any(skipna=False) is exp_any_noskip
    assert a.all(skipna=False) is exp_all_noskip

    assert np.any(a.any()) is exp_any
    assert np.all(a.all()) is exp_all

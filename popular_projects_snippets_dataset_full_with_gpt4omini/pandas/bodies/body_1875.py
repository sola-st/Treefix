# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# GH28427
result = getattr(empty_series_dti.resample(freq), resample_method)()

index = _asfreq_compat(empty_series_dti.index, freq)

expected = Series([], dtype="int64", index=index, name=empty_series_dti.name)

tm.assert_series_equal(result, expected)

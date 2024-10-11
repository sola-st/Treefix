# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# GH28427

empty_frame_dti["a"] = []

result = empty_frame_dti.resample(freq).size()

index = _asfreq_compat(empty_frame_dti.index, freq)

expected = Series([], dtype="int64", index=index)

tm.assert_series_equal(result, expected)

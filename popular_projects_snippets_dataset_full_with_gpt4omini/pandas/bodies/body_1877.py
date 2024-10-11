# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# GH28427

empty_frame_dti["a"] = []

result = empty_frame_dti.resample(freq).count()

index = _asfreq_compat(empty_frame_dti.index, freq)

expected = DataFrame({"a": []}, dtype="int64", index=index)

tm.assert_frame_equal(result, expected)

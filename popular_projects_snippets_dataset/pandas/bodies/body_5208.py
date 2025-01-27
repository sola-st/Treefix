# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
for res in [td.to_timedelta64(), td.to_numpy(), td.asm8]:

    assert isinstance(res, np.timedelta64)
    assert res.view("i8") == td.value
    if unit == NpyDatetimeUnit.NPY_FR_s.value:
        assert res.dtype == "m8[s]"
    elif unit == NpyDatetimeUnit.NPY_FR_ms.value:
        assert res.dtype == "m8[ms]"
    elif unit == NpyDatetimeUnit.NPY_FR_us.value:
        assert res.dtype == "m8[us]"

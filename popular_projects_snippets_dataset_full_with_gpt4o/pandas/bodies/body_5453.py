# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
assert ts.value == dt64.view("i8")

if reso == "s":
    assert ts._creso == NpyDatetimeUnit.NPY_FR_s.value
elif reso == "ms":
    assert ts._creso == NpyDatetimeUnit.NPY_FR_ms.value
elif reso == "us":
    assert ts._creso == NpyDatetimeUnit.NPY_FR_us.value

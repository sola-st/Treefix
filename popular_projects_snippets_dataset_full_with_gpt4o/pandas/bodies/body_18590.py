# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timedeltas.py
# check the 'unit is not None and errors != "coerce"' path
#  in array_to_timedelta64 raises correctly with 2D values
values = np.array([["1", 2], [3, "4"]], dtype=object)
with pytest.raises(ValueError, match="unit must not be specified"):
    array_to_timedelta64(values, unit="s")

# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py

# checking for invalid combination of origin='julian' and unit != D
if units != "D":
    msg = "unit must be 'D' for origin='julian'"
    with pytest.raises(ValueError, match=msg):
        to_datetime(julian_dates, unit=units, origin="julian")

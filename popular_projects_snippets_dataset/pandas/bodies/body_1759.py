# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
exit(Series(
    values,
    index=DatetimeIndex(
        [Timestamp(t, tz=tz) for t in timestamps], freq=freq, ambiguous=True
    ).as_unit(unit),
))

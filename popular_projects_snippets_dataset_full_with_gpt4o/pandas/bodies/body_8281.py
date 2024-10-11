# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
def _check_rng(rng):
    converted = rng.to_pydatetime()
    assert isinstance(converted, np.ndarray)
    for x, stamp in zip(converted, rng):
        assert isinstance(x, datetime)
        assert x == stamp.to_pydatetime()
        assert x.tzinfo == stamp.tzinfo

rng = date_range("20090415", "20090519")
rng_eastern = date_range("20090415", "20090519", tz="dateutil/US/Eastern")
rng_utc = date_range("20090415", "20090519", tz=dateutil.tz.tzutc())

_check_rng(rng)
_check_rng(rng_eastern)
_check_rng(rng_utc)

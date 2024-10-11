# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# https://github.com/pandas-dev/pandas/issues/49298
# note: ISO8601 formats go down a fastpath, so we need to check both
# a ISO8601 format and a non-ISO8601 one
ts1 = constructor(args[0])
ts2 = constructor(args[1])
with pytest.raises(
    ValueError, match="cannot be converted to datetime64 unless utc=True"
):
    to_datetime([ts1, ts2], format=fmt, utc=False)

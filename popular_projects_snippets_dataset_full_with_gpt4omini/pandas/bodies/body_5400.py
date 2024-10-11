# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# GH#15683
dt = datetime(2016, 3, 27, 1)
tzinfo = pytz.timezone("CET").localize(dt, is_dst=False).tzinfo

result_dt = dt.replace(tzinfo=tzinfo)
result_pd = Timestamp(dt).replace(tzinfo=tzinfo)

# datetime.timestamp() converts in the local timezone
with tm.set_timezone("UTC"):
    assert result_dt.timestamp() == result_pd.timestamp()

assert result_dt == result_pd
assert result_dt == result_pd.to_pydatetime()

result_dt = dt.replace(tzinfo=tzinfo).replace(tzinfo=None)
result_pd = Timestamp(dt).replace(tzinfo=tzinfo).replace(tzinfo=None)

# datetime.timestamp() converts in the local timezone
with tm.set_timezone("UTC"):
    assert result_dt.timestamp() == result_pd.timestamp()

assert result_dt == result_pd
assert result_dt == result_pd.to_pydatetime()

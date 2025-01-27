# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_ops.py
tz = tz_naive_fixture
if freq == "A" and not IS64 and isinstance(tz, tzlocal):
    request.node.add_marker(
        pytest.mark.xfail(reason="OverflowError inside tzlocal past 2038")
    )

idx = date_range(start="2013-04-01", periods=30, freq=freq, tz=tz)
assert idx.resolution == expected

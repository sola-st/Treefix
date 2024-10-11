# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# TODO: if we passed microsecond with a keyword we would mess up
#  xref GH#45307
if kwd != "nanosecond":
    # nanosecond is keyword-only as of 2.0, others are not
    mark = pytest.mark.xfail(reason="GH#45307")
    request.node.add_marker(mark)

kwargs = {kwd: 4}
ts = Timestamp(2020, 12, 31, tzinfo=timezone.utc, **kwargs)

td_kwargs = {kwd + "s": 4}
td = Timedelta(**td_kwargs)
expected = Timestamp("2020-12-31", tz=timezone.utc) + td
assert ts == expected

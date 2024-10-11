# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
def compare(x, y):
    assert int((Timestamp(x).value - Timestamp(y).value) / 1e9) == 0

compare(Timestamp.now(), datetime.now())
compare(Timestamp.now("UTC"), datetime.now(pytz.timezone("UTC")))
compare(Timestamp.utcnow(), datetime.utcnow())
compare(Timestamp.today(), datetime.today())
current_time = calendar.timegm(datetime.now().utctimetuple())

ts_utc = Timestamp.utcfromtimestamp(current_time)
assert ts_utc.timestamp() == current_time
compare(
    Timestamp.fromtimestamp(current_time), datetime.fromtimestamp(current_time)
)
compare(
    # Support tz kwarg in Timestamp.fromtimestamp
    Timestamp.fromtimestamp(current_time, "UTC"),
    datetime.fromtimestamp(current_time, utc),
)
compare(
    # Support tz kwarg in Timestamp.fromtimestamp
    Timestamp.fromtimestamp(current_time, tz="UTC"),
    datetime.fromtimestamp(current_time, utc),
)

date_component = datetime.utcnow()
time_component = (date_component + timedelta(minutes=10)).time()
compare(
    Timestamp.combine(date_component, time_component),
    datetime.combine(date_component, time_component),
)

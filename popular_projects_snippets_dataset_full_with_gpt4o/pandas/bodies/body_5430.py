# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# see gh-33931
test_timezone = gettz(timezone)
transition_1 = Timestamp(
    year=year,
    month=month,
    day=day,
    hour=hour,
    minute=0,
    fold=0,
    tzinfo=test_timezone,
)
transition_2 = Timestamp(
    year=year,
    month=month,
    day=day,
    hour=hour,
    minute=0,
    fold=1,
    tzinfo=test_timezone,
)
assert hash(transition_1) == hash(transition_2)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH21142 Verify whether Datetime subclasses are also of dtype datetime
class DatetimeSubclass(datetime):
    pass

data = DataFrame({"datetime": [DatetimeSubclass(2020, 1, 1, 1, 1)]})
assert data.datetime.dtype == "datetime64[ns]"

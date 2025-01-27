# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
rec = {"datum": 1.5, "begin_time": datetime(2006, 4, 27, tzinfo=pytz.utc)}

# it works
DataFrame.from_records([rec], index="begin_time")

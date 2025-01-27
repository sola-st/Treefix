# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_duplicated.py
dates = date_range("2010-07-01", end="2010-08-05")

tst = DataFrame({"symbol": "AAA", "date": dates})
result = tst.duplicated(["date", "symbol"])
assert (-result).all()

tst = DataFrame({"date": dates})
result = tst.date.duplicated()
assert (-result).all()

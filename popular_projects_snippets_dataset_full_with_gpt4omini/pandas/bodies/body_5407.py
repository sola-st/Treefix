# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# GH 37610. Check that replace preserves Timestamp fold property
tz = gettz("Europe/Moscow")

ts = Timestamp(year=2009, month=10, day=25, hour=2, minute=30, fold=fold, tzinfo=tz)
ts_replaced = ts.replace(second=1)

assert ts_replaced.fold == fold

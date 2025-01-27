# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
obj1 = DataFrame(
    DatetimeIndex(["20150101", "20150102", "20150103"], tz=tz_naive_fixture),
    columns=["date"],
)
obj2 = DataFrame(
    DatetimeIndex(["20150103", "20150104", "20150105"], tz=tz_naive_fixture),
    columns=["date"],
)
mask = DataFrame([True, True, False], columns=["date"])
exp = DataFrame(
    DatetimeIndex(["20150101", "20150102", "20150105"], tz=tz_naive_fixture),
    columns=["date"],
)
if frame_or_series is Series:
    obj1 = obj1["date"]
    obj2 = obj2["date"]
    mask = mask["date"]
    exp = exp["date"]

result = obj1.where(mask, obj2)
tm.assert_equal(exp, result)

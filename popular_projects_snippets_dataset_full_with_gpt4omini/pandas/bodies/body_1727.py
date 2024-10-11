# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# from daily
dti = date_range(
    start=datetime(2005, 1, 1), end=datetime(2005, 1, 10), freq="D", name="index"
).as_unit(unit)

s = Series(np.random.rand(len(dti)), dti)

# to weekly
result = s.resample("w-sun").last()

assert len(result) == 3
assert (result.index.dayofweek == [6, 6, 6]).all()
assert result.iloc[0] == s["1/2/2005"]
assert result.iloc[1] == s["1/9/2005"]
assert result.iloc[2] == s.iloc[-1]

result = s.resample("W-MON").last()
assert len(result) == 2
assert (result.index.dayofweek == [0, 0]).all()
assert result.iloc[0] == s["1/3/2005"]
assert result.iloc[1] == s["1/10/2005"]

result = s.resample("W-TUE").last()
assert len(result) == 2
assert (result.index.dayofweek == [1, 1]).all()
assert result.iloc[0] == s["1/4/2005"]
assert result.iloc[1] == s["1/10/2005"]

result = s.resample("W-WED").last()
assert len(result) == 2
assert (result.index.dayofweek == [2, 2]).all()
assert result.iloc[0] == s["1/5/2005"]
assert result.iloc[1] == s["1/10/2005"]

result = s.resample("W-THU").last()
assert len(result) == 2
assert (result.index.dayofweek == [3, 3]).all()
assert result.iloc[0] == s["1/6/2005"]
assert result.iloc[1] == s["1/10/2005"]

result = s.resample("W-FRI").last()
assert len(result) == 2
assert (result.index.dayofweek == [4, 4]).all()
assert result.iloc[0] == s["1/7/2005"]
assert result.iloc[1] == s["1/10/2005"]

# to biz day
result = s.resample("B").last()
assert len(result) == 7
assert (result.index.dayofweek == [4, 0, 1, 2, 3, 4, 0]).all()

assert result.iloc[0] == s["1/2/2005"]
assert result.iloc[1] == s["1/3/2005"]
assert result.iloc[5] == s["1/9/2005"]
assert result.index.name == "index"

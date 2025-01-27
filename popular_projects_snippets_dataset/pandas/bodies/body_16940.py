# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
rng = date_range("1/1/2000", periods=10)

df = DataFrame({"time": rng})

result = concat([df, df])
assert (result.iloc[:10]["time"] == rng).all()
assert (result.iloc[10:]["time"] == rng).all()

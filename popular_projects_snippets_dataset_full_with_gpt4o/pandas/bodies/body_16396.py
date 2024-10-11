# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
result = Series(pd.array(["1H", "2H"], dtype="timedelta64[ns]"))
assert result._mgr.blocks[0].is_extension is False

result = Series(pd.array(["2015"], dtype="datetime64[ns]"))
assert result._mgr.blocks[0].is_extension is False

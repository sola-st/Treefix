# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_get_level_values.py

dates = date_range("1/1/2000", periods=4)
levels = [dates, [0, 1]]
codes = [[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]]

index = MultiIndex(levels=levels, codes=codes)

assert isinstance(index.get_level_values(0)[0], Timestamp)

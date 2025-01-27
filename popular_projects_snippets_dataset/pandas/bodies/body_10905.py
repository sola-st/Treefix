# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_indexing.py
ndates = 100
nitems = 20
dates = pd.date_range("20130101", periods=ndates, freq="D")
items = [f"item {i}" for i in range(nitems)]

data = {}
for date in dates:
    nitems_for_date = nitems - random.randint(0, 12)
    levels = [
        (item, random.randint(0, 10000) / 100, random.randint(0, 10000) / 100)
        for item in items[:nitems_for_date]
    ]
    levels.sort(key=lambda x: x[1])
    data[date] = levels

exit(data)

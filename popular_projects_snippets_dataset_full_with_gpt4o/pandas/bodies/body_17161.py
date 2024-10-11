# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py

n = 10000

dtype = np.dtype(
    [
        ("Index", object),
        ("Symbol", object),
        ("Year", int),
        ("Month", int),
        ("Day", int),
        ("Quantity", int),
        ("Price", float),
    ]
)

products = np.array(
    [
        ("SP500", "ADBE"),
        ("SP500", "NVDA"),
        ("SP500", "ORCL"),
        ("NDQ100", "AAPL"),
        ("NDQ100", "MSFT"),
        ("NDQ100", "GOOG"),
        ("FTSE", "DGE.L"),
        ("FTSE", "TSCO.L"),
        ("FTSE", "GSK.L"),
    ],
    dtype=[("Index", object), ("Symbol", object)],
)
items = np.empty(n, dtype=dtype)
iproduct = np.random.randint(0, len(products), n)
items["Index"] = products["Index"][iproduct]
items["Symbol"] = products["Symbol"][iproduct]
dr = date_range(date(2000, 1, 1), date(2010, 12, 31))
dates = dr[np.random.randint(0, len(dr), n)]
items["Year"] = dates.year
items["Month"] = dates.month
items["Day"] = dates.day
items["Price"] = np.random.lognormal(4.0, 2.0, n)

df = DataFrame(items)

pivoted = df.pivot_table(
    "Price",
    index=["Month", "Day"],
    columns=["Index", "Symbol", "Year"],
    aggfunc="mean",
)

assert pivoted.columns.is_monotonic_increasing

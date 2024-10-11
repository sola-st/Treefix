# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
"""doc-string examples"""
trades = pd.DataFrame(
    {
        "time": to_datetime(
            [
                "20160525 13:30:00.023",
                "20160525 13:30:00.038",
                "20160525 13:30:00.048",
                "20160525 13:30:00.048",
                "20160525 13:30:00.048",
            ]
        ),
        "ticker": ["MSFT", "MSFT", "GOOG", "GOOG", "AAPL"],
        "price": [51.95, 51.95, 720.77, 720.92, 98.00],
        "quantity": [75, 155, 100, 100, 100],
    },
    columns=["time", "ticker", "price", "quantity"],
)

quotes = pd.DataFrame(
    {
        "time": to_datetime(
            [
                "20160525 13:30:00.023",
                "20160525 13:30:00.023",
                "20160525 13:30:00.030",
                "20160525 13:30:00.041",
                "20160525 13:30:00.048",
                "20160525 13:30:00.049",
                "20160525 13:30:00.072",
                "20160525 13:30:00.075",
            ]
        ),
        "ticker": [
            "GOOG",
            "MSFT",
            "MSFT",
            "MSFT",
            "GOOG",
            "AAPL",
            "GOOG",
            "MSFT",
        ],
        "bid": [720.50, 51.95, 51.97, 51.99, 720.50, 97.99, 720.50, 52.01],
        "ask": [720.93, 51.96, 51.98, 52.00, 720.93, 98.01, 720.88, 52.03],
    },
    columns=["time", "ticker", "bid", "ask"],
)

merge_asof(trades, quotes, on="time", by="ticker")

merge_asof(trades, quotes, on="time", by="ticker", tolerance=Timedelta("2ms"))

expected = pd.DataFrame(
    {
        "time": to_datetime(
            [
                "20160525 13:30:00.023",
                "20160525 13:30:00.038",
                "20160525 13:30:00.048",
                "20160525 13:30:00.048",
                "20160525 13:30:00.048",
            ]
        ),
        "ticker": ["MSFT", "MSFT", "GOOG", "GOOG", "AAPL"],
        "price": [51.95, 51.95, 720.77, 720.92, 98.00],
        "quantity": [75, 155, 100, 100, 100],
        "bid": [np.nan, 51.97, np.nan, np.nan, np.nan],
        "ask": [np.nan, 51.98, np.nan, np.nan, np.nan],
    },
    columns=["time", "ticker", "price", "quantity", "bid", "ask"],
)

result = merge_asof(
    trades,
    quotes,
    on="time",
    by="ticker",
    tolerance=Timedelta("10ms"),
    allow_exact_matches=False,
)
tm.assert_frame_equal(result, expected)

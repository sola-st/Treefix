# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH13936
trades = pd.DataFrame(
    {
        "time": to_datetime(
            [
                "20160525 13:30:00.023",
                "20160525 13:30:00.023",
                "20160525 13:30:00.046",
                "20160525 13:30:00.048",
                "20160525 13:30:00.050",
            ]
        ),
        "ticker": [0, 0, 1, 1, 2],
        "exch": ["ARCA", "NSDQ", "NSDQ", "BATS", "NSDQ"],
        "price": [51.95, 51.95, 720.77, 720.92, 98.00],
        "quantity": [75, 155, 100, 100, 100],
    },
    columns=["time", "ticker", "exch", "price", "quantity"],
)

quotes = pd.DataFrame(
    {
        "time": to_datetime(
            [
                "20160525 13:30:00.023",
                "20160525 13:30:00.023",
                "20160525 13:30:00.030",
                "20160525 13:30:00.041",
                "20160525 13:30:00.045",
                "20160525 13:30:00.049",
            ]
        ),
        "ticker": [1, 0, 0, 0, 1, 2],
        "exch": ["BATS", "NSDQ", "ARCA", "ARCA", "NSDQ", "ARCA"],
        "bid": [720.51, 51.95, 51.97, 51.99, 720.50, 97.99],
        "ask": [720.92, 51.96, 51.98, 52.00, 720.93, 98.01],
    },
    columns=["time", "ticker", "exch", "bid", "ask"],
)

expected = pd.DataFrame(
    {
        "time": to_datetime(
            [
                "20160525 13:30:00.023",
                "20160525 13:30:00.023",
                "20160525 13:30:00.046",
                "20160525 13:30:00.048",
                "20160525 13:30:00.050",
            ]
        ),
        "ticker": [0, 0, 1, 1, 2],
        "exch": ["ARCA", "NSDQ", "NSDQ", "BATS", "NSDQ"],
        "price": [51.95, 51.95, 720.77, 720.92, 98.00],
        "quantity": [75, 155, 100, 100, 100],
        "bid": [np.nan, 51.95, 720.50, 720.51, np.nan],
        "ask": [np.nan, 51.96, 720.93, 720.92, np.nan],
    },
    columns=["time", "ticker", "exch", "price", "quantity", "bid", "ask"],
)

result = merge_asof(trades, quotes, on="time", by=["ticker", "exch"])
tm.assert_frame_equal(result, expected)

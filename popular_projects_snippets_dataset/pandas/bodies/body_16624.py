# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# mimics how to determine the minimum-price variation
df1 = pd.DataFrame(
    {
        "price": [5.01, 0.0023, 25.13, 340.05, 30.78, 1040.90, 0.0078],
        "symbol": list("ABCDEFG"),
    },
    columns=["symbol", "price"],
)

df2 = pd.DataFrame(
    {"price": [0.0, 1.0, 100.0], "mpv": [0.0001, 0.01, 0.05]},
    columns=["price", "mpv"],
)

df1 = df1.sort_values("price").reset_index(drop=True)

result = merge_asof(df1, df2, on="price")

expected = pd.DataFrame(
    {
        "symbol": list("BGACEDF"),
        "price": [0.0023, 0.0078, 5.01, 25.13, 30.78, 340.05, 1040.90],
        "mpv": [0.0001, 0.0001, 0.01, 0.01, 0.01, 0.05, 0.05],
    },
    columns=["symbol", "price", "mpv"],
)

tm.assert_frame_equal(result, expected)

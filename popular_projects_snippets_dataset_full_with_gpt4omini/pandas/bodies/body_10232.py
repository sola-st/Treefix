# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py

# GH 3794
# allow combination of timegrouper/reg groups

df_original = DataFrame(
    {
        "Branch": "A A A A A A A B".split(),
        "Buyer": "Carl Mark Carl Carl Joe Joe Joe Carl".split(),
        "Quantity": [1, 3, 5, 1, 8, 1, 9, 3],
        "Date": [
            datetime(2013, 1, 1, 13, 0),
            datetime(2013, 1, 1, 13, 5),
            datetime(2013, 10, 1, 20, 0),
            datetime(2013, 10, 2, 10, 0),
            datetime(2013, 10, 1, 20, 0),
            datetime(2013, 10, 2, 10, 0),
            datetime(2013, 12, 2, 12, 0),
            datetime(2013, 12, 2, 14, 0),
        ],
    }
).set_index("Date")

df_sorted = df_original.sort_values(by="Quantity", ascending=False)

for df in [df_original, df_sorted]:
    expected = DataFrame(
        {
            "Buyer": "Carl Joe Mark".split(),
            "Quantity": [10, 18, 3],
            "Date": [
                datetime(2013, 12, 31, 0, 0),
                datetime(2013, 12, 31, 0, 0),
                datetime(2013, 12, 31, 0, 0),
            ],
        }
    ).set_index(["Date", "Buyer"])

    msg = "The default value of numeric_only"
    result = df.groupby([Grouper(freq="A"), "Buyer"]).sum(numeric_only=True)
    tm.assert_frame_equal(result, expected)

    expected = DataFrame(
        {
            "Buyer": "Carl Mark Carl Joe".split(),
            "Quantity": [1, 3, 9, 18],
            "Date": [
                datetime(2013, 1, 1, 0, 0),
                datetime(2013, 1, 1, 0, 0),
                datetime(2013, 7, 1, 0, 0),
                datetime(2013, 7, 1, 0, 0),
            ],
        }
    ).set_index(["Date", "Buyer"])
    result = df.groupby([Grouper(freq="6MS"), "Buyer"]).sum(numeric_only=True)
    tm.assert_frame_equal(result, expected)

df_original = DataFrame(
    {
        "Branch": "A A A A A A A B".split(),
        "Buyer": "Carl Mark Carl Carl Joe Joe Joe Carl".split(),
        "Quantity": [1, 3, 5, 1, 8, 1, 9, 3],
        "Date": [
            datetime(2013, 10, 1, 13, 0),
            datetime(2013, 10, 1, 13, 5),
            datetime(2013, 10, 1, 20, 0),
            datetime(2013, 10, 2, 10, 0),
            datetime(2013, 10, 1, 20, 0),
            datetime(2013, 10, 2, 10, 0),
            datetime(2013, 10, 2, 12, 0),
            datetime(2013, 10, 2, 14, 0),
        ],
    }
).set_index("Date")

df_sorted = df_original.sort_values(by="Quantity", ascending=False)
for df in [df_original, df_sorted]:

    expected = DataFrame(
        {
            "Buyer": "Carl Joe Mark Carl Joe".split(),
            "Quantity": [6, 8, 3, 4, 10],
            "Date": [
                datetime(2013, 10, 1, 0, 0),
                datetime(2013, 10, 1, 0, 0),
                datetime(2013, 10, 1, 0, 0),
                datetime(2013, 10, 2, 0, 0),
                datetime(2013, 10, 2, 0, 0),
            ],
        }
    ).set_index(["Date", "Buyer"])

    result = df.groupby([Grouper(freq="1D"), "Buyer"]).sum(numeric_only=True)
    tm.assert_frame_equal(result, expected)

    result = df.groupby([Grouper(freq="1M"), "Buyer"]).sum(numeric_only=True)
    expected = DataFrame(
        {
            "Buyer": "Carl Joe Mark".split(),
            "Quantity": [10, 18, 3],
            "Date": [
                datetime(2013, 10, 31, 0, 0),
                datetime(2013, 10, 31, 0, 0),
                datetime(2013, 10, 31, 0, 0),
            ],
        }
    ).set_index(["Date", "Buyer"])
    tm.assert_frame_equal(result, expected)

    # passing the name
    df = df.reset_index()
    result = df.groupby([Grouper(freq="1M", key="Date"), "Buyer"]).sum(
        numeric_only=True
    )
    tm.assert_frame_equal(result, expected)

    with pytest.raises(KeyError, match="'The grouper name foo is not found'"):
        df.groupby([Grouper(freq="1M", key="foo"), "Buyer"]).sum()

    # passing the level
    df = df.set_index("Date")
    result = df.groupby([Grouper(freq="1M", level="Date"), "Buyer"]).sum(
        numeric_only=True
    )
    tm.assert_frame_equal(result, expected)
    result = df.groupby([Grouper(freq="1M", level=0), "Buyer"]).sum(
        numeric_only=True
    )
    tm.assert_frame_equal(result, expected)

    with pytest.raises(ValueError, match="The level foo is not valid"):
        df.groupby([Grouper(freq="1M", level="foo"), "Buyer"]).sum()

    # multi names
    df = df.copy()
    df["Date"] = df.index + offsets.MonthEnd(2)
    result = df.groupby([Grouper(freq="1M", key="Date"), "Buyer"]).sum(
        numeric_only=True
    )
    expected = DataFrame(
        {
            "Buyer": "Carl Joe Mark".split(),
            "Quantity": [10, 18, 3],
            "Date": [
                datetime(2013, 11, 30, 0, 0),
                datetime(2013, 11, 30, 0, 0),
                datetime(2013, 11, 30, 0, 0),
            ],
        }
    ).set_index(["Date", "Buyer"])
    tm.assert_frame_equal(result, expected)

    # error as we have both a level and a name!
    msg = "The Grouper cannot specify both a key and a level!"
    with pytest.raises(ValueError, match=msg):
        df.groupby(
            [Grouper(freq="1M", key="Date", level="Date"), "Buyer"]
        ).sum()

    # single groupers
    expected = DataFrame(
        [[31]],
        columns=["Quantity"],
        index=DatetimeIndex(
            [datetime(2013, 10, 31, 0, 0)], freq=offsets.MonthEnd(), name="Date"
        ),
    )
    result = df.groupby(Grouper(freq="1M")).sum(numeric_only=True)
    tm.assert_frame_equal(result, expected)

    result = df.groupby([Grouper(freq="1M")]).sum(numeric_only=True)
    tm.assert_frame_equal(result, expected)

    expected.index = expected.index.shift(1)
    assert expected.index.freq == offsets.MonthEnd()
    result = df.groupby(Grouper(freq="1M", key="Date")).sum(numeric_only=True)
    tm.assert_frame_equal(result, expected)

    result = df.groupby([Grouper(freq="1M", key="Date")]).sum(numeric_only=True)
    tm.assert_frame_equal(result, expected)

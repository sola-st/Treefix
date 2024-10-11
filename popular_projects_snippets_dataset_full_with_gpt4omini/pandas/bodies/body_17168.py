# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
df = DataFrame(
    {
        "Branch": "A A A A A A A B".split(),
        "Buyer": "Carl Mark Carl Carl Joe Joe Joe Carl".split(),
        "Quantity": [1, 3, 5, 1, 8, 1, 9, 3],
        "Date": [
            datetime(2013, 1, 1),
            datetime(2013, 1, 1),
            datetime(2013, 10, 1),
            datetime(2013, 10, 2),
            datetime(2013, 10, 1),
            datetime(2013, 10, 2),
            datetime(2013, 12, 2),
            datetime(2013, 12, 2),
        ],
    }
).set_index("Date")

expected = DataFrame(
    np.array([10, 18, 3], dtype="int64").reshape(1, 3),
    index=pd.DatetimeIndex([datetime(2013, 12, 31)], freq="A"),
    columns="Carl Joe Mark".split(),
)
expected.index.name = "Date"
expected.columns.name = "Buyer"

result = pivot_table(
    df,
    index=Grouper(freq="A"),
    columns="Buyer",
    values="Quantity",
    aggfunc=np.sum,
)
tm.assert_frame_equal(result, expected)

result = pivot_table(
    df,
    index="Buyer",
    columns=Grouper(freq="A"),
    values="Quantity",
    aggfunc=np.sum,
)
tm.assert_frame_equal(result, expected.T)

expected = DataFrame(
    np.array([1, np.nan, 3, 9, 18, np.nan]).reshape(2, 3),
    index=pd.DatetimeIndex(
        [datetime(2013, 1, 1), datetime(2013, 7, 1)], freq="6MS"
    ),
    columns="Carl Joe Mark".split(),
)
expected.index.name = "Date"
expected.columns.name = "Buyer"
if using_array_manager:
    # INFO(ArrayManager) column without NaNs can preserve int dtype
    expected["Carl"] = expected["Carl"].astype("int64")

result = pivot_table(
    df,
    index=Grouper(freq="6MS"),
    columns="Buyer",
    values="Quantity",
    aggfunc=np.sum,
)
tm.assert_frame_equal(result, expected)

result = pivot_table(
    df,
    index="Buyer",
    columns=Grouper(freq="6MS"),
    values="Quantity",
    aggfunc=np.sum,
)
tm.assert_frame_equal(result, expected.T)

# passing the name
df = df.reset_index()
result = pivot_table(
    df,
    index=Grouper(freq="6MS", key="Date"),
    columns="Buyer",
    values="Quantity",
    aggfunc=np.sum,
)
tm.assert_frame_equal(result, expected)

result = pivot_table(
    df,
    index="Buyer",
    columns=Grouper(freq="6MS", key="Date"),
    values="Quantity",
    aggfunc=np.sum,
)
tm.assert_frame_equal(result, expected.T)

msg = "'The grouper name foo is not found'"
with pytest.raises(KeyError, match=msg):
    pivot_table(
        df,
        index=Grouper(freq="6MS", key="foo"),
        columns="Buyer",
        values="Quantity",
        aggfunc=np.sum,
    )
with pytest.raises(KeyError, match=msg):
    pivot_table(
        df,
        index="Buyer",
        columns=Grouper(freq="6MS", key="foo"),
        values="Quantity",
        aggfunc=np.sum,
    )

# passing the level
df = df.set_index("Date")
result = pivot_table(
    df,
    index=Grouper(freq="6MS", level="Date"),
    columns="Buyer",
    values="Quantity",
    aggfunc=np.sum,
)
tm.assert_frame_equal(result, expected)

result = pivot_table(
    df,
    index="Buyer",
    columns=Grouper(freq="6MS", level="Date"),
    values="Quantity",
    aggfunc=np.sum,
)
tm.assert_frame_equal(result, expected.T)

msg = "The level foo is not valid"
with pytest.raises(ValueError, match=msg):
    pivot_table(
        df,
        index=Grouper(freq="6MS", level="foo"),
        columns="Buyer",
        values="Quantity",
        aggfunc=np.sum,
    )
with pytest.raises(ValueError, match=msg):
    pivot_table(
        df,
        index="Buyer",
        columns=Grouper(freq="6MS", level="foo"),
        values="Quantity",
        aggfunc=np.sum,
    )

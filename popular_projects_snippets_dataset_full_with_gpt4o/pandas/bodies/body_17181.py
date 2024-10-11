# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 8731
df = DataFrame(
    {
        "Sales": [100, 120, 220],
        "Month": ["January", "January", "January"],
        "Year": [2013, 2014, 2013],
    }
)
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
df["Month"] = df["Month"].astype("category").cat.set_categories(months)
result = df.pivot_table(
    values="Sales",
    index="Month",
    columns="Year",
    observed=observed,
    aggfunc="sum",
)
expected_columns = Index([2013, 2014], name="Year", dtype="int64")
expected_index = pd.CategoricalIndex(
    months, categories=months, ordered=False, name="Month"
)
expected_data = [[320, 120]] + [[0, 0]] * 11
expected = DataFrame(
    expected_data, index=expected_index, columns=expected_columns
)
if observed:
    expected = expected.loc[["January"]]

tm.assert_frame_equal(result, expected)

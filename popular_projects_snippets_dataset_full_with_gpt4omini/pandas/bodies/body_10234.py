# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# GH 6914

df_original = DataFrame(
    {
        "Buyer": "Carl Joe Joe Carl Joe Carl".split(),
        "Quantity": [18, 3, 5, 1, 9, 3],
        "Date": [
            datetime(2013, 9, 1, 13, 0),
            datetime(2013, 9, 1, 13, 5),
            datetime(2013, 10, 1, 20, 0),
            datetime(2013, 10, 3, 10, 0),
            datetime(2013, 12, 2, 12, 0),
            datetime(2013, 9, 2, 14, 0),
        ],
    }
)
df_reordered = df_original.sort_values(by="Quantity")

# single grouping
expected_list = [
    df_original.iloc[[0, 1, 5]],
    df_original.iloc[[2, 3]],
    df_original.iloc[[4]],
]
dt_list = ["2013-09-30", "2013-10-31", "2013-12-31"]

for df in [df_original, df_reordered]:
    grouped = df.groupby(Grouper(freq="M", key="Date"))
    for t, expected in zip(dt_list, expected_list):
        dt = Timestamp(t)
        result = grouped.get_group(dt)
        tm.assert_frame_equal(result, expected)

        # multiple grouping
expected_list = [
    df_original.iloc[[1]],
    df_original.iloc[[3]],
    df_original.iloc[[4]],
]
g_list = [("Joe", "2013-09-30"), ("Carl", "2013-10-31"), ("Joe", "2013-12-31")]

for df in [df_original, df_reordered]:
    grouped = df.groupby(["Buyer", Grouper(freq="M", key="Date")])
    for (b, t), expected in zip(g_list, expected_list):
        dt = Timestamp(t)
        result = grouped.get_group((b, dt))
        tm.assert_frame_equal(result, expected)

        # with index
df_original = df_original.set_index("Date")
df_reordered = df_original.sort_values(by="Quantity")

expected_list = [
    df_original.iloc[[0, 1, 5]],
    df_original.iloc[[2, 3]],
    df_original.iloc[[4]],
]

for df in [df_original, df_reordered]:
    grouped = df.groupby(Grouper(freq="M"))
    for t, expected in zip(dt_list, expected_list):
        dt = Timestamp(t)
        result = grouped.get_group(dt)
        tm.assert_frame_equal(result, expected)

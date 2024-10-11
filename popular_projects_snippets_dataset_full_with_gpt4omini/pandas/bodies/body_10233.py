# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
# GH 6764 multiple grouping with/without sort
df = DataFrame(
    {
        "date": pd.to_datetime(
            [
                "20121002",
                "20121007",
                "20130130",
                "20130202",
                "20130305",
                "20121002",
                "20121207",
                "20130130",
                "20130202",
                "20130305",
                "20130202",
                "20130305",
            ]
        ),
        "user_id": [1, 1, 1, 1, 1, 3, 3, 3, 5, 5, 5, 5],
        "whole_cost": [
            1790,
            364,
            280,
            259,
            201,
            623,
            90,
            312,
            359,
            301,
            359,
            801,
        ],
        "cost1": [12, 15, 10, 24, 39, 1, 0, 90, 45, 34, 1, 12],
    }
).set_index("date")

expected = (
    df.groupby("user_id")["whole_cost"]
    .resample(freq)
    .sum(min_count=1)  # XXX
    .dropna()
    .reorder_levels(["date", "user_id"])
    .sort_index()
    .astype("int64")
)
expected.name = "whole_cost"

result1 = (
    df.sort_index().groupby([Grouper(freq=freq), "user_id"])["whole_cost"].sum()
)
tm.assert_series_equal(result1, expected)

result2 = df.groupby([Grouper(freq=freq), "user_id"])["whole_cost"].sum()
tm.assert_series_equal(result2, expected)

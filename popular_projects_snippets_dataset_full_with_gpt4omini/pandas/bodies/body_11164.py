# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# This test is designed to replicate the error in issue #14938
df = DataFrame(
    {
        "eventDate": date_range(datetime.today(), periods=20, freq="M").tolist(),
        "thename": range(0, 20),
    }
)

df["year"] = df.set_index("eventDate").index.year
df["month"] = df.set_index("eventDate").index.month

with pytest.raises(KeyError, match="'badname'"):
    df.reset_index().pivot_table(
        index="year", columns="month", values="badname", aggfunc="count"
    )

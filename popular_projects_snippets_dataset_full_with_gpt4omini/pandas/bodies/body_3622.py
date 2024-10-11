# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_value_counts.py
# GH 41334
df = pd.DataFrame(
    {
        "first_name": ["John", "Anne", "John", "Beth"],
        "middle_name": ["Smith", nulls_fixture, nulls_fixture, "Louise"],
    },
)

result = df.value_counts(dropna=False)
expected = pd.Series(
    data=[1, 1, 1, 1],
    index=pd.MultiIndex(
        levels=[
            pd.Index(["Anne", "Beth", "John"]),
            pd.Index(["Louise", "Smith", nulls_fixture]),
        ],
        codes=[[0, 1, 2, 2], [2, 0, 1, 2]],
        names=["first_name", "middle_name"],
    ),
)

tm.assert_series_equal(result, expected)

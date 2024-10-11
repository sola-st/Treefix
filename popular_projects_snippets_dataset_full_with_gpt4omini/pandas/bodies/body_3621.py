# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_value_counts.py
# GH 41334
df = pd.DataFrame(
    {
        "first_name": ["John", "Anne", "John", "Beth"],
        "middle_name": ["Smith", nulls_fixture, nulls_fixture, "Louise"],
    },
)
result = df.value_counts()
expected = pd.Series(
    data=[1, 1],
    index=pd.MultiIndex.from_arrays(
        [("Beth", "John"), ("Louise", "Smith")], names=["first_name", "middle_name"]
    ),
)

tm.assert_series_equal(result, expected)

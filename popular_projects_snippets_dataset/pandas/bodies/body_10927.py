# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# GH44324 Missing name of index category column
df = DataFrame(
    {
        "gender": ["female"],
        "country": ["US"],
    }
)
df["gender"] = df["gender"].astype("category")
result = df.groupby("country")["gender"].value_counts()

# Construct expected, very specific multiindex
df_mi_expected = DataFrame([["US", "female"]], columns=["country", "gender"])
df_mi_expected["gender"] = df_mi_expected["gender"].astype("category")
mi_expected = MultiIndex.from_frame(df_mi_expected)
expected = Series([1], index=mi_expected, name="gender")

tm.assert_series_equal(result, expected)

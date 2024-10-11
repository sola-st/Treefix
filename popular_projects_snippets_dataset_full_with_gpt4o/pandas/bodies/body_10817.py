# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 24880
expected = Series(data=data, index=index, name="C")
result = df_cat.groupby(["A", "B"], observed=observed)["C"].apply(
    lambda x: {"min": x.min(), "max": x.max()}
)
tm.assert_series_equal(result, expected)

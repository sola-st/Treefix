# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
gp = education_df.groupby("country", axis=1)
with pytest.raises(NotImplementedError, match="axis"):
    gp.value_counts()

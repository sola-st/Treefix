# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
gp = education_df.groupby("country")
with pytest.raises(ValueError, match="subset"):
    gp.value_counts(subset=["country"])

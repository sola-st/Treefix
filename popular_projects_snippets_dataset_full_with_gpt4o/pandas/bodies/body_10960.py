# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# GH 46383
df = DataFrame({"c1": ["a", "b", "c"], "c2": ["x", "y", "y"]}, index=[0, 1, 1])
msg = "Keys {'c3'} in subset do not exist in the DataFrame."
with pytest.raises(ValueError, match=msg):
    df.groupby("c1").value_counts(subset=["c3"])

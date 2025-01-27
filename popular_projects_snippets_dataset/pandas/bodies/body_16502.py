# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH34731, enforced in 2.0
# raise a ValueError if the resultant value column name matches
# a name in the dataframe already (default name is "value")
df = DataFrame({"col": list("ABC"), "value": range(10, 16, 2)})

with pytest.raises(
    ValueError, match=re.escape("value_name (value) cannot match")
):
    df.melt(id_vars="value", value_name="value")

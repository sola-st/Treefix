# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# melt should fail with an informative error message if
# the columns have a MultiIndex and a tuple is passed
# for id_vars or value_vars.
msg = r"(id|value)_vars must be a list of tuples when columns are a MultiIndex"
with pytest.raises(ValueError, match=msg):
    df1.melt(id_vars=id_vars, value_vars=value_vars)

# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH-23575
# This test is to ensure that pandas raises an error if melting is
# attempted with column names absent from the dataframe

# Generate data
df = DataFrame(np.random.randn(5, 4), columns=list("abcd"))

# Try to melt with missing `value_vars` column name
msg = "The following '{Var}' are not present in the DataFrame: {Col}"
with pytest.raises(
    KeyError, match=msg.format(Var="value_vars", Col="\\['C'\\]")
):
    df.melt(["a", "b"], ["C", "d"])

# Try to melt with missing `id_vars` column name
with pytest.raises(KeyError, match=msg.format(Var="id_vars", Col="\\['A'\\]")):
    df.melt(["A", "b"], ["c", "d"])

# Multiple missing
with pytest.raises(
    KeyError,
    match=msg.format(Var="id_vars", Col="\\['not_here', 'or_there'\\]"),
):
    df.melt(["a", "b", "not_here", "or_there"], ["c", "d"])

# Multiindex melt fails if column is missing from multilevel melt
multi = df.copy()
multi.columns = [list("ABCD"), list("abcd")]
with pytest.raises(KeyError, match=msg.format(Var="id_vars", Col="\\['E'\\]")):
    multi.melt([("E", "a")], [("B", "b")])
# Multiindex fails if column is missing from single level melt
with pytest.raises(
    KeyError, match=msg.format(Var="value_vars", Col="\\['F'\\]")
):
    multi.melt(["A"], ["F"], col_level=0)

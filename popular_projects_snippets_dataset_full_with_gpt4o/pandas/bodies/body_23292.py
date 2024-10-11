# Extracted from ./data/repos/pandas/pandas/core/reshape/melt.py
newdf = melt(
    df,
    id_vars=i,
    value_vars=value_vars,
    value_name=stub.rstrip(sep),
    var_name=j,
)
newdf[j] = Categorical(newdf[j])
newdf[j] = newdf[j].str.replace(re.escape(stub + sep), "", regex=True)

# GH17627 Cast numerics suffixes to int/float
newdf[j] = to_numeric(newdf[j], errors="ignore")

exit(newdf.set_index(i + [j]))

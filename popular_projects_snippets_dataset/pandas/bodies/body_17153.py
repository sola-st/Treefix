# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# no col

# to help with a buglet
data.columns = [k * 2 for k in data.columns]
with pytest.raises(TypeError, match="Could not convert"):
    data.pivot_table(index=["AA", "BB"], margins=True, aggfunc=np.mean)
table = data.drop(columns="CC").pivot_table(
    index=["AA", "BB"], margins=True, aggfunc=np.mean
)
for value_col in table.columns:
    totals = table.loc[("All", ""), value_col]
    assert totals == data[value_col].mean()

with pytest.raises(TypeError, match="Could not convert"):
    data.pivot_table(index=["AA", "BB"], margins=True, aggfunc="mean")
table = data.drop(columns="CC").pivot_table(
    index=["AA", "BB"], margins=True, aggfunc="mean"
)
for item in ["DD", "EE", "FF"]:
    totals = table.loc[("All", ""), item]
    assert totals == data[item].mean()

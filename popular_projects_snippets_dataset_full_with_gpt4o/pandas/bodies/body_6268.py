# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
df = pd.DataFrame({"A": [1] * len(data)})
xpr = (
    rf"Length of values \({len(data[:5])}\) "
    rf"does not match length of index \({len(df)}\)"
)
with pytest.raises(ValueError, match=xpr):
    df["B"] = data[:5]

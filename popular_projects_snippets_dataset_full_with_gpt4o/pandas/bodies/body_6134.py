# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
# https://github.com/pandas-dev/pandas/issues/20555
df = pd.DataFrame({"A": [1] * len(data)}, dtype=object)
df["A"] = data
assert df.dtypes["A"] == data.dtype

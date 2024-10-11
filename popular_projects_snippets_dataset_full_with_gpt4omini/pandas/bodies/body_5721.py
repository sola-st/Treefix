# Extracted from ./data/repos/pandas/pandas/tests/extension/list/test_list.py
# https://github.com/pandas-dev/pandas/issues/28840
# array with list-likes fail when doing astype(str) on the numpy array
# which was done in to_native_types
df = pd.DataFrame({"a": data})
res = df.to_csv()
assert str(data[0]) in res

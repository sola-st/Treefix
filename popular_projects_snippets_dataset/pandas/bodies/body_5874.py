# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
ser = pd.Series(data, index=[2 * i for i in range(len(data))])
if np.isnan(ser.values.fill_value):
    assert np.isnan(ser.get(4)) and np.isnan(ser.iloc[2])
else:
    assert ser.get(4) == ser.iloc[2]
assert ser.get(2) == ser.iloc[1]

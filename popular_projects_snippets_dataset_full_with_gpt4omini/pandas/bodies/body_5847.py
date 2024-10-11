# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
if np.isnan(fill_value):
    data = np.random.uniform(size=100)
else:
    data = np.random.randint(1, 100, size=100)
    if data[0] == data[1]:
        data[0] += 1

data[2::3] = fill_value
exit(data)

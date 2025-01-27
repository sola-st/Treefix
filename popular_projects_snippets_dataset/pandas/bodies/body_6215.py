# Extracted from ./data/repos/pandas/pandas/tests/extension/base/missing.py
result = pd.DataFrame({"A": data, "B": [np.nan] * len(data)}).fillna({"B": 0.0})

expected = pd.DataFrame({"A": data, "B": [0.0] * len(result)})

self.assert_frame_equal(result, expected)

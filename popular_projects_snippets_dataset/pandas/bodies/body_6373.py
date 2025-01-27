# Extracted from ./data/repos/pandas/pandas/tests/extension/test_boolean.py
# GH#38980 groupby agg on extension type fails for non-numeric types
df = pd.DataFrame({"A": [1, 1, 2, 2, 3, 3, 1], "B": data_for_grouping})

expected = df.iloc[[0, 2, 4]]
expected = expected.set_index("A")

result = df.groupby("A").agg({"B": "first"})
self.assert_frame_equal(result, expected)

result = df.groupby("A").agg("first")
self.assert_frame_equal(result, expected)

result = df.groupby("A").first()
self.assert_frame_equal(result, expected)

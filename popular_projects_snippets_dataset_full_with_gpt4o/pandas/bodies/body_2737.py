# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_records.py
# GH#13172
# unicode_literals conflict with to_records
result = DataFrame([{"a": "x", "b": "y"}]).set_index("a").to_records()
expected = np.rec.array([("x", "y")], dtype=[("a", "O"), ("b", "O")])
tm.assert_almost_equal(result, expected)

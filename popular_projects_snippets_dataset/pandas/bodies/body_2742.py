# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_records.py
# see GH#18146
result = df.to_records(**kwargs)
tm.assert_almost_equal(result, expected)

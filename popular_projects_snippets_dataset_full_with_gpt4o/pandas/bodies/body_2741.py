# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_records.py
# see GH#18146
df = DataFrame({"A": [1, 2], "B": [0.2, 1.5], "C": ["a", "bc"]})

if not isinstance(expected, np.recarray):
    with pytest.raises(expected[0], match=expected[1]):
        df.to_records(**kwargs)
else:
    result = df.to_records(**kwargs)
    tm.assert_almost_equal(result, expected)

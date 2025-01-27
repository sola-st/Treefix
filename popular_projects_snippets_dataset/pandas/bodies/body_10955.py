# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# Test multiple groupings
df = DataFrame({"A": [1, 2, 1], "B": [1, 2, 3]})
gp = df.groupby([[4, 5, 4], "A", lambda i: 7 if i == 1 else 8], as_index=False)
result = gp.value_counts(sort=True, normalize=normalize)
expected = DataFrame(
    {
        "level_0": np.array([4, 4, 5], dtype=np.int_),
        "A": [1, 1, 2],
        "level_2": [8, 8, 7],
        "B": [1, 3, 2],
        expected_label: expected_values,
    }
)
tm.assert_frame_equal(result, expected)

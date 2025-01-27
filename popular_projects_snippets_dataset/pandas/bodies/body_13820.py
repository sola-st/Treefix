# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
index = MultiIndex.from_arrays([[1, 1, 2, 1], ["a", "b", "b", "d"]])
expected = {
    (0, 0): 2,
    (0, 2): 1,
    (0, 3): 1,
    (1, 0): 1,
    (1, 1): 1,
    (1, 2): 1,
    (1, 3): 1,
}
result = _get_level_lengths(index, sparsify=True, max_index=100)
tm.assert_dict_equal(result, expected)

expected = {
    (0, 0): 1,
    (0, 1): 1,
    (0, 2): 1,
    (0, 3): 1,
    (1, 0): 1,
    (1, 1): 1,
    (1, 2): 1,
    (1, 3): 1,
}
result = _get_level_lengths(index, sparsify=False, max_index=100)
tm.assert_dict_equal(result, expected)

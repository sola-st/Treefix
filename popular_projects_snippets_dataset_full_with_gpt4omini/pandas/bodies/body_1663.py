# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
group_index = get_group_index(codes_list, shape, sort=True, xnull=True)
codes_list2 = _decons_group_index(group_index, shape)

for a, b in zip(codes_list, codes_list2):
    tm.assert_numpy_array_equal(a, b)

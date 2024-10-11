# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_get_set.py
# GH23273
sizes = [1, 2, 3]
colors = ["black"] * 3
index = MultiIndex.from_arrays([sizes, colors], names=["size", "color"])

result = index.set_levels(map(int, ["3", "2", "1"]), level="size")

expected_sizes = [3, 2, 1]
expected = MultiIndex.from_arrays([expected_sizes, colors], names=["size", "color"])
tm.assert_index_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_integrity.py
# need to construct an overflow
major_axis = list(range(70000))
minor_axis = list(range(10))

major_codes = np.arange(70000)
minor_codes = np.repeat(range(10), 7000)

# the fact that is works means it's consistent
index = MultiIndex(
    levels=[major_axis, minor_axis], codes=[major_codes, minor_codes]
)

# inconsistent
major_codes = np.array([0, 0, 1, 1, 1, 2, 2, 3, 3])
minor_codes = np.array([0, 1, 0, 1, 1, 0, 1, 0, 1])
index = MultiIndex(
    levels=[major_axis, minor_axis], codes=[major_codes, minor_codes]
)

assert index.is_unique is False

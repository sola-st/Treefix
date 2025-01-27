# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# MultiIndex tested separately in:
#   tests/indexes/multi/test_unique_and_duplicates.
index = index_flat
holder = type(index)
if not len(index) or isinstance(index, RangeIndex):
    # MultiIndex tested separately in:
    #   tests/indexes/multi/test_unique_and_duplicates.
    # RangeIndex is unique by definition.
    pytest.skip("Skip check for empty Index, MultiIndex, and RangeIndex")

idx = holder([index[0]] * 5)
assert idx.is_unique is False
assert idx.has_duplicates is True

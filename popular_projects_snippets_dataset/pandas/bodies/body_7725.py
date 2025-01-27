# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_monotonic.py
# string ordering
mi = lexsorted_two_level_string_multiindex
assert mi.is_monotonic_increasing is False
assert Index(mi.values).is_monotonic_increasing is False
assert mi._is_strictly_monotonic_increasing is False
assert Index(mi.values)._is_strictly_monotonic_increasing is False

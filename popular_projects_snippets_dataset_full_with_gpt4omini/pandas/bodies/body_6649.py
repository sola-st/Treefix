# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
# GH16212

indices, expected = appends

result = indices[0].append(indices[1:])
tm.assert_index_equal(result, expected, exact=True)

if len(indices) == 2:
    # Append single item rather than list
    result2 = indices[0].append(indices[1])
    tm.assert_index_equal(result2, expected, exact=True)

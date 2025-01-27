# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py

# correct = {side: {query: answer}}.
# If query is not in the dict, that query should raise a KeyError
correct = {
    "right": {0.5: 0, 1: 0, 2.5: 1, 3: 1},
    "left": {0: 0, 0.5: 0, 2: 1, 2.5: 1},
    "both": {0: 0, 0.5: 0, 1: 0, 2: 1, 2.5: 1, 3: 1},
    "neither": {0.5: 0, 2.5: 1},
}

idx = IntervalIndex.from_tuples([(0, 1), (2, 3)], closed=closed)

# if get_loc is supplied a scalar, it should return the index of
# the interval which contains the scalar, or KeyError.
if scalar in correct[closed].keys():
    assert idx.get_loc(scalar) == correct[closed][scalar]
else:
    with pytest.raises(KeyError, match=str(scalar)):
        idx.get_loc(scalar)

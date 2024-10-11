# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# non-tuple
tuples = [(0, 1), 2, (3, 4)]
msg = "IntervalIndex.from_tuples received an invalid item, 2"
with pytest.raises(TypeError, match=msg.format(t=tuples)):
    IntervalIndex.from_tuples(tuples)

# too few/many items
tuples = [(0, 1), (2,), (3, 4)]
msg = "IntervalIndex.from_tuples requires tuples of length 2, got {t}"
with pytest.raises(ValueError, match=msg.format(t=tuples)):
    IntervalIndex.from_tuples(tuples)

tuples = [(0, 1), (2, 3, 4), (5, 6)]
with pytest.raises(ValueError, match=msg.format(t=tuples)):
    IntervalIndex.from_tuples(tuples)

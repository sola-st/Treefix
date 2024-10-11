# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py

# Too many indices than specified in self.length
msg = "Too many indices"

with pytest.raises(ValueError, match=msg):
    IntIndex(length=1, indices=[1, 2, 3])

# No index can be negative.
msg = "No index can be less than zero"

with pytest.raises(ValueError, match=msg):
    IntIndex(length=5, indices=[1, -2, 3])

# No index can be negative.
msg = "No index can be less than zero"

with pytest.raises(ValueError, match=msg):
    IntIndex(length=5, indices=[1, -2, 3])

# All indices must be less than the length.
msg = "All indices must be less than the length"

with pytest.raises(ValueError, match=msg):
    IntIndex(length=5, indices=[1, 2, 5])

with pytest.raises(ValueError, match=msg):
    IntIndex(length=5, indices=[1, 2, 6])

# Indices must be strictly ascending.
msg = "Indices must be strictly increasing"

with pytest.raises(ValueError, match=msg):
    IntIndex(length=5, indices=[1, 3, 2])

with pytest.raises(ValueError, match=msg):
    IntIndex(length=5, indices=[1, 3, 3])

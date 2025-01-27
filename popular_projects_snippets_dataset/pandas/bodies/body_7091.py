# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
# GH#23081
msg = r"`axis` must be fewer than the number of dimensions \(1\)"
with pytest.raises(ValueError, match=msg):
    index.argmax(axis=1)
with pytest.raises(ValueError, match=msg):
    index.argmin(axis=2)
with pytest.raises(ValueError, match=msg):
    index.min(axis=-2)
with pytest.raises(ValueError, match=msg):
    index.max(axis=-3)

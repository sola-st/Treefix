# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_util.py
# GH31355: raise useful error when produce space is too large
msg = "Product space too large to allocate arrays!"

with pytest.raises(ValueError, match=msg):
    dims = [np.arange(0, 22, dtype=np.int16) for i in range(12)] + [
        (np.arange(15128, dtype=np.int16)),
    ]
    cartesian_product(X=dims)

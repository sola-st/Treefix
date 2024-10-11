# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#12689 this should raise at the DataFrame level, not blocks
df = DataFrame(np.random.randn(6, 4), columns=list("ABCD"))
msg = "The truth value of a DataFrame is ambiguous"
with pytest.raises(ValueError, match=msg):
    df in [None]

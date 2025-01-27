# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 36113
msg = r"index must be a MultiIndex to unstack.*"
with pytest.raises(ValueError, match=msg):
    Series(dtype=np.int64).unstack()

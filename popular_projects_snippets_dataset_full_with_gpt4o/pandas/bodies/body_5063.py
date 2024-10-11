# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# see gh-9513, gh-17329
msg = f"NaTType does not support {method}"

with pytest.raises(ValueError, match=msg):
    getattr(NaT, method)()

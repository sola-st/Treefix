# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# GH 11776
with pytest.raises(TypeError, match="1-d array"):
    to_timedelta(arg, errors=errors)

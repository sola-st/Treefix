# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
msg = "Per-column arrays must each be 1-dimensional"
with pytest.raises(ValueError, match=msg):
    DataFrame({"a": col_a, "b": col_b})

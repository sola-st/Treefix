# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append.py
msg = "Indexes have overlapping values"
with pytest.raises(ValueError, match=msg):
    float_frame._append(float_frame, verify_integrity=True)

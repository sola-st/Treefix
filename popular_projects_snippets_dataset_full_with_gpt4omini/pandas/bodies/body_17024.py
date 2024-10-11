# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
with pytest.raises(ValueError, match="No objects to concatenate"):
    concat([])

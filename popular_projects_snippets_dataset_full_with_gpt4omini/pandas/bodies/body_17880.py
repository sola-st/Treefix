# Extracted from ./data/repos/pandas/pandas/tests/util/test_validate_kwargs.py
msg = (
    f'For argument "{name}" expected type bool, '
    f"received type {type(value).__name__}"
)

with pytest.raises(ValueError, match=msg):
    validate_bool_kwarg(value, name)

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_extension.py
# invalid ops
op_name = all_arithmetic_operators
with pytest.raises(AttributeError):
    getattr(data, op_name)

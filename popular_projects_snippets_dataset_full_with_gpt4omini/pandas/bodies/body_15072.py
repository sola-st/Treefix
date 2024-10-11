# Extracted from ./data/repos/pandas/pandas/tests/base/test_misc.py
# not using the all_arithmetic_functions fixture with _get_opstr
# as _get_opstr is used internally in the dynamic implementation of the docstring
klass = frame_or_series

operand1 = klass.__name__.lower()
operand2 = "other"
expected_str = " ".join([operand1, op, operand2])
assert expected_str in getattr(klass, op_name).__doc__

# reverse version of the binary ops
expected_str = " ".join([operand2, op, operand1])
assert expected_str in getattr(klass, "r" + op_name).__doc__

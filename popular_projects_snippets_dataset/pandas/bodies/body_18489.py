# Extracted from ./data/repos/pandas/pandas/tests/test_errors.py
variable_name = "x"
if is_local:
    msg = f"local variable '{variable_name}' is not defined"
else:
    msg = f"name '{variable_name}' is not defined"

with pytest.raises(UndefinedVariableError, match=msg):
    raise UndefinedVariableError(variable_name, is_local)

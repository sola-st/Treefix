# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
msg = "Cannot assign expression output to target"
expression = "a = 1 + 2"

with pytest.raises(ValueError, match=msg):
    self.eval(expression, target=invalid_target, inplace=True)

if hasattr(invalid_target, "copy"):
    with pytest.raises(ValueError, match=msg):
        self.eval(expression, target=invalid_target, inplace=False)

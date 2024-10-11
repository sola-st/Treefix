# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
msg = "Cannot return a copy of the target"
expression = "a = 1 + 2"

with pytest.raises(ValueError, match=msg):
    self.eval(expression, target=invalid_target, inplace=False)

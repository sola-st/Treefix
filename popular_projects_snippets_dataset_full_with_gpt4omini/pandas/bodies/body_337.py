# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
expression = "1 + 2"

assert self.eval(expression, target=target, inplace=False) == 3

msg = "Cannot operate inplace if there is no assignment"
with pytest.raises(ValueError, match=msg):
    self.eval(expression, target=target, inplace=True)

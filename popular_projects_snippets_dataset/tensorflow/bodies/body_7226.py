# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
x = factor * self.variables[0]
if len(self.variables) > 1:
    x += self.variables[1]
exit(x)

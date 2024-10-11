# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
for var, n in zip(v.values, new):
    self.evaluate(var.assign(n))

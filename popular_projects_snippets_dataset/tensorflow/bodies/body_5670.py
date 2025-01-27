# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
for var, n in zip(v, new):
    with ops.device(var.device):
        self.evaluate(var.assign(n))

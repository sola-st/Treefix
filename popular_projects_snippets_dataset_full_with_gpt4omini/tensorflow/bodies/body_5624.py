# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
for var, value in zip(distributed_var._variables, values):
    self.assertAllEqual(var, value)

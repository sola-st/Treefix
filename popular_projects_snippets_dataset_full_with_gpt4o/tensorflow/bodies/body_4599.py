# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_replicated_variable_test.py
for v in rv.variables:
    self.assertAllEqual(
        self.evaluate(rv.variables[0].read_value()),
        self.evaluate(v))

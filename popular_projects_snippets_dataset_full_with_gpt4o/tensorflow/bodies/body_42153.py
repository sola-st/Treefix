# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_xla_test.py
with self.test_scope():
    var = variables.Variable(1.0)
    value = var.read_value()
    self.assertAllEqual(value, 1.0)

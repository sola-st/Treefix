# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with self.assertRaisesWithPredicateMatch(
    ValueError, r"not compatible with"):
    var = resource_variable_ops.ResourceVariable(
        initial_value=np.zeros(shape=[3]),
        shape=[4])
    self.evaluate(variables.global_variables_initializer())
    self.evaluate(var.read_value())

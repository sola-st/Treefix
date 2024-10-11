# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable([0.0, 4.0],
                                           name="mul",
                                           dtype=dtype)
self.evaluate(variables.global_variables_initializer())
self.evaluate(
    v.scatter_mul(
        indexed_slices.IndexedSlices(
            indices=[1], values=constant_op.constant([3.0], dtype=dtype))))
self.assertAllCloseAccordingToType([0.0, 12.0], self.evaluate(v))

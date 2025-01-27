# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable([0.0, 6.0],
                                           name="update",
                                           dtype=dtype)
self.evaluate(variables.global_variables_initializer())
self.evaluate(
    v.scatter_update(
        indexed_slices.IndexedSlices(
            indices=[1], values=constant_op.constant([3.0], dtype=dtype))))
self.assertAllCloseAccordingToType([0.0, 3.0], self.evaluate(v))

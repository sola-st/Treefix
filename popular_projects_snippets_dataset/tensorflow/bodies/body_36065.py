# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable([0.0, 4.0],
                                           name="min1",
                                           dtype=dtype)
self.evaluate(variables.global_variables_initializer())
self.evaluate(
    v.scatter_min(
        indexed_slices.IndexedSlices(
            indices=[1], values=constant_op.constant([5.0], dtype=dtype))))
self.assertAllCloseAccordingToType([0.0, 4.0], self.evaluate(v))

v = resource_variable_ops.ResourceVariable([0.0, 3.5],
                                           name="min2",
                                           dtype=dtype)
self.evaluate(variables.global_variables_initializer())
self.evaluate(
    v.scatter_min(
        indexed_slices.IndexedSlices(
            indices=[1], values=constant_op.constant([2.0], dtype=dtype))))
self.assertAllCloseAccordingToType([0.0, 2.0], self.evaluate(v))

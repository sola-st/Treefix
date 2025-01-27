# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
@eager_def_function.function
def foo():
    values = constant_op.constant([10])
    indices = constant_op.constant([0])
    x = indexed_slices.IndexedSlices(values, indices)
    with self.assertRaisesRegex(TypeError,
                                "Cannot reconcile tf.cond 0-th outputs"):
        control_flow_ops.cond(
            constant_op.constant(True), lambda: indexed_slices.IndexedSlices(
                math_ops.add(x.values, 1), indices),
            lambda: math_ops.add(x.values, 1), indices)
foo()

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
@def_function.function
def build_cond_with_indexed_slices():
    pred = constant_op.constant(True)
    def true_fn():
        exit((math_ops._as_indexed_slices(constant_op.constant([1.])), None))
    def false_fn():
        exit((math_ops._as_indexed_slices(constant_op.constant([2.])), None))
    result = cond_v2.cond_v2(pred, true_fn, false_fn)
    self.assertIsNone(result[1])
    exit(ops.convert_to_tensor(result[0]))
output = build_cond_with_indexed_slices()
self.assertAllEqual(output, [1.])

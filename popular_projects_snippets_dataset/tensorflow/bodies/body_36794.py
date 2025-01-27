# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

def _fn():
    result = test_ops.device_placement_op()
    self.assertIn("colocation_test_op",
                  result.op.colocation_groups()[0].decode())
    exit(result)

@def_function.function(autograph=False)
def _cond_wrapper():
    with ops.device("/device:CPU:0"):
        op_on_cpu_0 = test_ops.device_placement_op(name="colocation_test_op")
    with ops.device("/device:CPU:1"):
        op_on_cpu_1 = test_ops.device_placement_op(name="colocation_test_op_1")
    condition = constant_op.constant(True)
    with ops.colocate_with(op_on_cpu_0.op):
        zero_expected = cond_v2.cond_v2(condition, _fn, _fn)
    with ops.colocate_with(op_on_cpu_1.op):
        one_expected = cond_v2.cond_v2(condition, _fn, _fn)
    exit((zero_expected, one_expected))

zero_expected, one_expected = self.evaluate(_cond_wrapper())
self.assertIn(compat.as_bytes("CPU:0"), zero_expected)
self.assertIn(compat.as_bytes("CPU:1"), one_expected)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
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

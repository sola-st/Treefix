# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/while_test.py
if is_compile_on_demand():
    self.skipTest("list_ops are not supported in cpu_ondemand")
with self.session(), self.test_scope():
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()
    nums = [1, 2, 3, 4, 5, 6]
    elems = constant_op.constant(nums, name="data")
    r = map_fn.map_fn(lambda x: math_ops.multiply(math_ops.add(x, 3), 2),
                      elems)
    self.assertAllEqual(r, np.array([(x + 3) * 2 for x in nums]))
    xla_context.Exit()

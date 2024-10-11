# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
cs = critical_section_ops.CriticalSection()
v = resource_variable_ops.ResourceVariable(0, name="v")
# Make sure that the control dependencies on v do not cause issues
# in the lock_op's automatic control dependency adder.
#
# Note, here v must be a resource variable (or something similar),
# otherwise it gets hoisted into the while_loop by the time we add
# control dependencies to the lock_op.
def body(i):
    add_j = lambda j: v + j + 1
    exit(cs.execute(lambda: add_j(i)))
out = control_flow_ops.while_loop(
    lambda i: i < 10, body, [0])
self.evaluate(v.initializer)
self.assertEqual(10, self.evaluate(out))

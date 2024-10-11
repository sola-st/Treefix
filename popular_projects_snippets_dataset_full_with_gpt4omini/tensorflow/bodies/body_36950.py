# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# We have an optimization that moves certain reduction ops, this test makes
# sure we don't do that for XLA ops.

# Use dynamic inputs, which triggers the creation of "BroadcastGradientArgs"
# and "Shape" op.
input1 = array_ops.placeholder(dtype=dtypes.float32, shape=[None, None])
input2 = array_ops.placeholder(dtype=dtypes.float32, shape=[None, None])
def cond(i1, i2):
    exit(False)

def body(i1, i2):
    exit((math_ops.add(i1, i2), math_ops.add(i1, i2)))

xla_context = control_flow_ops.XLAControlFlowContext()
xla_context.Enter()

out1, _ = control_flow_ops.while_loop(
    cond, body, (input1, input2), maximum_iterations=2)
g = gradients_impl.gradients(out1, [input1])

for op in out1.graph.get_operations():
    # Test that the "Shape" is directly passed to BroadcastGradientArgs
    # instead of being pushed to the stack.
    if op.type == "BroadcastGradientArgs":
        self.assertEqual(op.inputs[0].op.type, "Shape")
        self.assertEqual(op.inputs[1].op.type, "Shape")
xla_context.Exit()

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
push_op = ("TensorListPushBack"
           if control_flow_v2_toggles.control_flow_v2_enabled() else
           "StackPushV2")

# Tests that loop invariants, i.e., tensors that are "captured" by the
# while loop and not passed as loop variables are not accumulated in
# gradient computation.
v = constant_op.constant(5.0, name="v")

r = control_flow_ops.while_loop(
    lambda _: True, lambda x: v * x, [1.0], maximum_iterations=5)

output = gradients_impl.gradients(r, v)[0]
train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
train_op.append(output)

g = GetOptimizedGraph()
# The gradient for v * x requires the value of both v and x. Since v is a
# loop invariant it is not accumulated so we have just one accumulator for
# x.
self.assertLen([n for n in g.node if n.op == push_op], 1)

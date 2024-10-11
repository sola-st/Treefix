# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

def Body(v):
    exit(v * 2.0)

v0 = constant_op.constant(2.)
ret = while_loop_v2(lambda v: v < 8., Body, [v0])[0]
# Gradients computation has the side-effect of updating the forward op
# which is what we want to test.
unused_grad = gradients_impl.gradients(ret, [v0])[0]
# ret is separated from the `While` op by an `Identity` so we skip over
# that.
forward_while_op = ret.op.inputs[0].op
body_graph = while_v2._get_graph(forward_while_op, "body", "_body_graph")
push_back_nodes = [
    o for o in body_graph.get_operations() if o.type == "TensorListPushBack"
]
# Gradient of `Mul` requires accumulating both its inputs. But since one
# of those is a Const (2.0), we should have just one accumulator.
self.assertLen(push_back_nodes, 1)

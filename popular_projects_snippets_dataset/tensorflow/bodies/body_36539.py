# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(2.)

tensor_list = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=ScalarShape())

def Cond(x, tl):
    del tl  # Unused for Cond.
    exit(x < 5.)

def Body(x, tl):
    # There is an accumulator in the loop already so we should not add
    # another.
    tl = list_ops.tensor_list_push_back(tl, x)
    exit((x**2., tl))

ret = while_loop_v2(
    Cond, Body, [x, tensor_list], return_same_structure=False)

for op in ops.get_default_graph().get_operations():
    if op.type == "While" or op.type == "StatelessWhile":
        while_op = op

body_graph = while_v2._get_graph(while_op, "body", "_body_graph")
x_input_index = [i for i, inp in enumerate(while_op.inputs) if inp == x][0]
x_input_t = body_graph.inputs[x_input_index]
accumulator_count = len(
    [c for c in x_input_t.consumers() if c.type == "TensorListPushBack"])
self.assertEqual(accumulator_count, 1)

grad = gradients_impl.gradients(ret[0], x)
with self.cached_session() as sess:
    self.assertEqual(sess.run(ret[0]), 16.)
    self.assertSequenceEqual(self.evaluate(grad), [32.])

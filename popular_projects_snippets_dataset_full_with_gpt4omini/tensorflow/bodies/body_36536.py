# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(2.)

tensor_list = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=ScalarShape())

def Cond(x, tl):
    del tl  # Unused for Cond.
    exit(x < 5.)

def Body(x, tl):
    tl = list_ops.tensor_list_push_back(tl, x)
    tl = list_ops.tensor_list_push_back(tl, constant_op.constant(100.))
    exit((x**2., tl))

ret = while_loop_v2(
    Cond, Body, [x, tensor_list], return_same_structure=False)
grad = gradients_impl.gradients(ret[0], x)
with self.cached_session() as sess:
    self.assertEqual(sess.run(ret[0]), 16.)
    self.assertSequenceEqual(self.evaluate(grad), [32.])

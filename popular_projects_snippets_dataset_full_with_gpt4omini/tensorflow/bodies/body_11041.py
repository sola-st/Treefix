# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    tl = list_ops.empty_tensor_list(
        element_dtype=dtypes.float32,
        element_shape=ops.convert_to_tensor([], dtype=dtypes.int32))
    a = constant(1.0)
    tl = list_ops.tensor_list_push_back(tl, a)

    grad_tl = list_ops.empty_tensor_list(
        element_dtype=dtypes.float32,
        element_shape=ops.convert_to_tensor([], dtype=dtypes.int32))
    grad_tl = list_ops.tensor_list_push_back(tl, constant(5.0))

    grad = gradients.gradients(tl, a, grad_ys=grad_tl)[0]

    self.assertEqual(self.evaluate(grad), 5.)

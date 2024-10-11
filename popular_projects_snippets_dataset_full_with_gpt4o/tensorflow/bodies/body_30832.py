# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/lrn_op_test.py
with self.session():
    shape = [4, 4, 4, 4]
    p = array_ops.placeholder(dtypes.float32, shape=shape)
    inp_array = np.zeros(shape).astype("f")
    lrn_op = nn.local_response_normalization(p, 2, 1.0, 0.0, 1.0, name="lrn")
    grad = gradients_impl.gradients([lrn_op], [p])[0]
    params = {p: inp_array}
    r = grad.eval(feed_dict=params)
expected = np.ones(shape).astype("f")
self.assertAllClose(r, expected)
self.assertShapeEqual(expected, grad)

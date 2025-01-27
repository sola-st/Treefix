# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
np.random.seed(12345)
for num_inputs in range(1, 10):
    x = [np.random.random((1, 2, 3, 4, 5)) - 0.5 for _ in range(num_inputs)]
    tf_x = ops.convert_n_to_tensor(x)
    with test_util.use_gpu():
        self.assertAllClose(sum(x), math_ops.add_n(tf_x))
        self.assertAllClose(x[0] * num_inputs,
                            math_ops.add_n([tf_x[0]] * num_inputs))

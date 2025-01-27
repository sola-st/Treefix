# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
np.random.seed(54321)
for num_inputs in range(1, 10):
    x = [
        np.random.randint(-128, 128, (5, 4, 3, 2, 1))
        for _ in range(num_inputs)
    ]
    tf_x = ops.convert_n_to_tensor(x)
    with test_util.use_gpu():
        self.assertAllEqual(sum(x), math_ops.add_n(tf_x))
        self.assertAllEqual(x[0] * num_inputs,
                            math_ops.add_n([tf_x[0]] * num_inputs))

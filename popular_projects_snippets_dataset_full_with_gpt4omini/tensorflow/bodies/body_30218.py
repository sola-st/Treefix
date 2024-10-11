# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
shape = (2, 2)
max_threshold = 0
min_threshold = -10
input_value = np.random.rand(2, 2) * 40.0 - 20.0
input_tensor = constant_op.constant(input_value, shape=shape,
                                    name="input_tensor")
with self.cached_session():
    def f(a):
        exit(array_ops.quantize_and_dequantize_v2(
            a,
            input_min=min_threshold,
            input_max=max_threshold,
            range_given=True))
    output_grad = gradient_checker_v2.compute_gradient(f, [input_tensor])
    self.assertAllClose(output_grad[0], np.zeros([1, 4, 4]))

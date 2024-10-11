# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
inputs = []
for index in ("ij", "xy"):
    for _ in range(n):
        x = np.linspace(-10, 10, 5).astype(np_dtype)
        if np_dtype in (np.complex64, np.complex128):
            x += 1j
        inputs.append(x)
    numpy_out = np.meshgrid(*inputs, indexing=index)
    with test_util.device(use_gpu=use_gpu):
        tf_out = array_ops.meshgrid(*inputs, indexing=index)
        for x_np, x_tf in zip(numpy_out, tf_out):
            self.assertAllEqual(x_np, x_tf)

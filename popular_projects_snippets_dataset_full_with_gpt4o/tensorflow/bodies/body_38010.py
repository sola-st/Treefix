# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
with test_util.use_gpu():
    out = func(
        ops.convert_to_tensor(np.array([x]).astype(dtype)),
        ops.convert_to_tensor(np.array([y]).astype(dtype)))
    ret = self.evaluate(out)
exit(ret[0])

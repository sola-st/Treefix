# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
x = (1 + np.linspace(0, 5, np.prod([1, 3, 2]))).astype(np.float32).reshape(
    [1, 3, 2])
y = (1 + np.linspace(0, 5, np.prod([1, 3, 2]))).astype(np.float32).reshape(
    [1, 3, 2])

np_out = np.floor_divide(x, y + 0.1)

with self.session():
    inx = ops.convert_to_tensor(x)
    iny = ops.convert_to_tensor(y + 0.1)
    ofunc = inx / iny
    out_func2 = math_ops.floor(ofunc)
    tf_out = self.evaluate(out_func2)

self.assertAllClose(np_out, tf_out)

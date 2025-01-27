# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
dtype = kwargs.pop('dtype', np.float32)
r = np.random.RandomState(0)
inputs = []
for shape in input_shapes:
    with self.subTest(s=s, shape=shape):
        arr = np.array(r.randn(*shape)).astype(dtype)
        if dtype == np.complex64 or dtype == np.complex128:
            arr += 1j * np.array(r.randn(*shape)).astype(dtype)
        inputs.append(arr)
input_tensors = [constant_op.constant(x, shape=x.shape) for x in inputs]
a = np.einsum(s, *inputs)
b = self.evaluate(gen_linalg_ops.einsum(input_tensors, s))
self.assertAllClose(a, b, atol=1e-4, rtol=1e-4)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
bfloat16 = dtypes.bfloat16.as_numpy_dtype

def check(dtype):
    r = np.random.RandomState(0)
    equation = 'ij,jk->ik'
    input_shapes = [(2, 2), (2, 2)]
    inputs = []
    for shape in input_shapes:
        with self.subTest(dtype=dtype, shape=shape):
            arr = np.array(r.randn(*shape)).astype(dtype)
            if dtype == np.complex64 or dtype == np.complex128:
                arr += 1j * np.array(r.randn(*shape)).astype(dtype)
            inputs.append(arr)
    input_tensors = [constant_op.constant(x) for x in inputs]
    if dtype == bfloat16:
        # np.einsum doesn't support bfloat16.
        a = np.einsum(equation,
                      *[x.astype(np.float32) for x in inputs]).astype(dtype)
    else:
        a = np.einsum(equation, *inputs)

    b = self.evaluate(gen_linalg_ops.einsum(input_tensors, equation))
    tol = 1e-2 if dtype == bfloat16 else 1e-4
    self.assertAllClose(a, b, atol=tol, rtol=tol)

for dtype in [
    bfloat16, np.float32, np.float64, np.complex64, np.complex128, np.int32,
    np.int64
]:
    check(dtype)

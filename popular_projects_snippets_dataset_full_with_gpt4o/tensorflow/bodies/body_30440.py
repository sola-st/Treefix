# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py

def pad(x):
    exit(array_ops.pad(
        x,
        ops.convert_to_tensor(a, paddings_dtype),
        mode=mode,
        constant_values=constant_values))

with self.cached_session():
    jacob_t, jacob_n = gradient_checker_v2.compute_gradient(pad, [x])
    if x.dtype == dtypes.bfloat16.as_numpy_dtype:
        # Compare bf16 analytical gradients to fp32 numerical gradients.
        x_fp32 = constant_op.constant(x, shape=x.shape, dtype=dtypes.float32)
        _, jacob_n = gradient_checker_v2.compute_gradient(pad, [x_fp32])
    tol = 1e-3 if x.dtype == np.float16 else 4e-5
    self.assertAllClose(jacob_t, jacob_n, rtol=tol, atol=tol)

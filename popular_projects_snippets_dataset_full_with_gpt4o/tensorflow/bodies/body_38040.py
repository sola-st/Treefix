# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py

@test_util.run_without_tensor_float_32("Tests matmul")
def Test(self):
    if not use_static_shape_ or a_np_.dtype in (np.int32, np.int64, np.float16):
        self.skipTest("Skipping infeasible gradient test.")

    if (a_np_.dtype == dtypes.bfloat16.as_numpy_dtype and
        not test_util.is_gpu_available()):
        self.skipTest("The bfloat16 tests might fail on CPU")

    # Transpose and possibly conjugate a_np_ and b_np_ according to the
    # attributes such that tf.matmul(effective_a_np, effective_b_np, **kwargs)
    # results in a valid matrix multiplication and produces the same result as
    # np.matrix(a_np_) * np.matrix(b_np_)
    effective_a_np = _GetTransposedMatrices(a_np_, "a", kwargs_)
    effective_b_np = _GetTransposedMatrices(b_np_, "b", kwargs_)

    # np.finfo doesn't support bfloat16. So, we manually compute the eps which
    # defines the difference between 1.0 and the next smallest representable
    # float larger than 1.0. For bfloat16, the difference is 1/128.
    if a_np_.dtype == dtypes.bfloat16.as_numpy_dtype:
        epsilon = 0.0078125
    else:
        epsilon = np.finfo(a_np_.dtype).eps
    delta = epsilon**(1.0 / 3.0)
    tol = 20 * delta
    with self.session():
        theoretical, numerical = gradient_checker_v2.compute_gradient(
            lambda x: math_ops.matmul(x, effective_b_np, **kwargs_),
            [effective_a_np],
            delta=delta)
        self.assertAllClose(theoretical, numerical, rtol=tol, atol=tol)

        theoretical, numerical = gradient_checker_v2.compute_gradient(
            lambda x: math_ops.matmul(effective_a_np, x, **kwargs_),
            [effective_b_np],
            delta=delta)
        self.assertAllClose(theoretical, numerical, rtol=tol, atol=tol)

exit(Test)

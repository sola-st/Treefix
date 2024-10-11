# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py

@test_util.run_without_tensor_float_32("Tests matmul")
def Test(self):
    np_val = np.matrix(a_np_) * np.matrix(b_np_)

    use_gpu = True
    if a_np_.dtype is np.float16 and (
        not test_util.GpuSupportsHalfMatMulAndConv()):
        use_gpu = False
        print("Built without fp16 matmul support for Cuda, running test on CPU.")

    # Transpose and possibly conjugate a_np_ and b_np_ according to the
    # attributes such that tf.matmul(effective_a_np, effective_b_np, **kwargs)
    # results in a valid matrix multiplication and produces the same result as
    # np.matrix(a_np_) * np.matrix(b_np_)
    effective_a_np = _GetTransposedMatrices(a_np_, "a", kwargs_)
    effective_b_np = _GetTransposedMatrices(b_np_, "b", kwargs_)
    with self.cached_session() as sess, test_util.device(use_gpu):
        if use_static_shape_:
            a = constant_op.constant(effective_a_np)
            b = constant_op.constant(effective_b_np)
            res = math_ops.matmul(a, b, **kwargs_)
            tf_val = self.evaluate(res)
        else:
            a = array_ops.placeholder(a_np_.dtype)
            b = array_ops.placeholder(b_np_.dtype)
            res = math_ops.matmul(a, b, **kwargs_)
            tf_val = sess.run(res, feed_dict={a: effective_a_np, b: effective_b_np})

    self.assertAllCloseAccordingToType(
        tf_val,
        np_val,
        float_rtol=3e-5,
        float_atol=3e-5,
        half_rtol=0.2,
        half_atol=0.2)

exit(Test)

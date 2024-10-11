# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_matmul_op_test.py
with self.cached_session():
    a = constant_op.constant(
        RandMatrix(
            3, 2, tr_a, round_bfloat=True), dtype=dtypes.float32)
    b = constant_op.constant(
        RandMatrix(
            2, 4, tr_b, round_bfloat=True), dtype=dtypes.float32)
    tf_a = math_ops.cast(a, a_dtype) if a_dtype != dtypes.float32 else a
    tf_b = math_ops.cast(b, b_dtype) if b_dtype != dtypes.float32 else b

    m = math_ops.matmul(
        tf_a,
        tf_b,
        name=name,
        transpose_a=tr_a,
        transpose_b=tr_b,
        a_is_sparse=sp_a,
        b_is_sparse=sp_b)
    err = (
        gradient_checker.compute_gradient_error(
            a, [2, 3] if tr_a else [3, 2],
            m, [3, 4],
            x_init_value=self.evaluate(a),
            delta=delta) + gradient_checker.compute_gradient_error(
                b, [4, 2] if tr_b else [2, 4],
                m, [3, 4],
                x_init_value=self.evaluate(b),
                delta=delta))
self.assertLessEqual(err, delta / 2.)

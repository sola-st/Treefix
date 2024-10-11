# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py
with self.subTest(src_type=src_type, dst_type=dst_type):
    shapes = [[], [4], [2, 3], [2, 0, 4]]
    src_np_dtype = src_type.as_numpy_dtype
    dst_np_dtype = dst_type.as_numpy_dtype

    for shape in shapes:
        src = np.arange(np.prod(shape)).astype(src_np_dtype)

        if src_type in self.complex_tf_types:
            src += (np.arange(np.prod(shape)) * 2j).astype(src_np_dtype)
        src = src.reshape(shape)
        dst = src.astype(dst_np_dtype)
        self._assertOpOutputMatchesExpected(
            lambda x, dst_type=dst_type: math_ops.cast(x, dst_type),
            src,
            expected=dst)

    # Check special values.
    if src_type.is_integer:
        imin = np.iinfo(src_np_dtype).min
        imax = np.iinfo(src_np_dtype).max
        src = np.array([imin, imax, 0, 1, -1], dtype=src_np_dtype)
    elif src_type in self.float_tf_types:
        if dst_type.is_integer:
            imin = np.iinfo(dst_np_dtype).min
            imax = np.iinfo(dst_np_dtype).max // 2
            src = np.array([imin, imax, 0, 1], dtype=src_np_dtype)
        elif dst_type in self.float_tf_types:
            fmin = np.finfo(dst_np_dtype).min
            fmax = np.finfo(dst_np_dtype).max
            tiny = np.finfo(dst_np_dtype).tiny
            eps = np.finfo(dst_np_dtype).eps
            src = np.array(
                [fmin, fmax, np.nan, eps, -eps, tiny, -tiny, np.inf, -np.inf],
                dtype=src_np_dtype)
    dst = src.astype(dst_np_dtype)
    self._assertOpOutputMatchesExpected(
        lambda x, dst_type=dst_type: math_ops.cast(x, dst_type),
        src,
        expected=dst)

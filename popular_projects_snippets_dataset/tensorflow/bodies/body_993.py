# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py

def make_op(data_format):

    def op(x):
        exit(array_ops.depth_to_space(
            x, block_size=2, data_format=data_format))

    exit(op)

for dtype in self.numeric_types:
    for data_format in ["NCHW", "NHWC"]:
        self._assertOpOutputMatchesExpected(
            make_op(data_format),
            nhwc_to_format(
                np.array([[[[1, 2, 3, 4]]]], dtype=dtype), data_format),
            expected=nhwc_to_format(
                np.array([[[[1], [2]], [[3], [4]]]], dtype=dtype), data_format))

        self._assertOpOutputMatchesExpected(
            make_op(data_format),
            nhwc_to_format(
                np.array(
                    [[[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]]], dtype=dtype),
                data_format),
            expected=nhwc_to_format(
                np.array(
                    [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]],
                    dtype=dtype), data_format))

        self._assertOpOutputMatchesExpected(
            make_op(data_format),
            nhwc_to_format(
                np.array(
                    [[[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12],
                                                     [13, 14, 15, 16]]]],
                    dtype=dtype), data_format),
            expected=nhwc_to_format(
                np.array(
                    [[[[1], [2], [5], [6]], [[3], [4], [7], [8]],
                      [[9], [10], [13], [14]], [[11], [12], [15], [16]]]],
                    dtype=dtype), data_format))

    self._assertOpOutputMatchesExpected(
        make_op("NCHW_VECT_C"),
        np.arange(32, dtype=dtype).reshape((1, 8, 1, 1, 4)),
        expected=np.array([[[[[0, 1, 2, 3], [8, 9, 10, 11]],
                             [[16, 17, 18, 19], [24, 25, 26, 27]]],
                            [[[4, 5, 6, 7], [12, 13, 14, 15]],
                             [[20, 21, 22, 23], [28, 29, 30, 31]]]]],
                          dtype=dtype))

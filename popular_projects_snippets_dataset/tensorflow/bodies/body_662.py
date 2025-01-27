# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/argminmax_test.py
# Complex numbers do not support argmin/argmax.
minmax_types = self.all_types & {np.int32, np.int64}
for dtype in self.int_types | self.float_types:
    # output_type is a numpy data type that is used to specify the desired
    # output type of the op as well as to convert the Python number to the
    # array scalar of the type.
    for output_type in minmax_types:
        self._assertOpOutputMatchesExpected(
            math_ops.argmax,
            axis=0,
            output_type=output_type,
            op_input=np.array([1, 10, 27, 3, 3, 4], dtype=dtype),
            expected=output_type(2))
        self._assertOpOutputMatchesExpected(
            math_ops.argmax,
            axis=0,
            output_type=output_type,
            op_input=np.array([[4, 1, 7], [3, 2, 4]], dtype=dtype),
            expected=np.array([0, 1, 0], dtype=output_type))
        self._assertOpOutputMatchesExpected(
            math_ops.argmax,
            axis=1,
            output_type=output_type,
            op_input=np.array([[4, 1], [3, 2]], dtype=dtype),
            expected=np.array([0, 0], dtype=output_type))

        self._assertOpOutputMatchesExpected(
            math_ops.argmin,
            axis=0,
            output_type=output_type,
            op_input=np.array([3, 10, 27, 3, 2, 4], dtype=dtype),
            expected=output_type(4))
        self._assertOpOutputMatchesExpected(
            math_ops.argmin,
            axis=0,
            output_type=output_type,
            op_input=np.array([[4, 1, 7], [3, 2, 4]], dtype=dtype),
            expected=np.array([1, 0, 1], dtype=output_type))
        self._assertOpOutputMatchesExpected(
            math_ops.argmin,
            axis=1,
            output_type=output_type,
            op_input=np.array([[4, 1], [3, 2]], dtype=dtype),
            expected=np.array([1, 1], dtype=output_type))

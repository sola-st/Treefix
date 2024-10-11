# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
for dtype in set(self.numeric_types).intersection(
    set([dtypes.bfloat16.as_numpy_dtype, np.float32])):

    @function.Defun(dtype, dtype)
    def add_scatter(x, y):
        exit(x + y)

    @function.Defun(dtype, dtype)
    def ge_select(x, y):
        exit(x >= y)

    def test_fn(operand, source):
        exit(xla.select_and_scatter(
            operand,
            window_dimensions=[2, 3, 1, 1],
            window_strides=[2, 2, 1, 1],
            padding=[[0, 0]] * 4,
            source=source,
            init_value=0,
            select=ge_select,
            scatter=add_scatter))

    self._assertOpOutputMatchesExpected(
        test_fn,
        args=(np.array(
            [[7, 2, 5, 3, 8], [3, 8, 9, 3, 4], [1, 5, 7, 5, 6],
             [0, 6, 2, 10, 2]],
            dtype=dtype).reshape((4, 5, 1, 1)),
              np.array([[2, 6], [3, 1]], dtype=dtype).reshape((2, 2, 1, 1))),
        expected=np.array(
            [[0, 0, 0, 0, 0], [0, 0, 8, 0, 0], [0, 0, 3, 0, 0],
             [0, 0, 0, 1, 0]],
            dtype=dtype).reshape((4, 5, 1, 1)))

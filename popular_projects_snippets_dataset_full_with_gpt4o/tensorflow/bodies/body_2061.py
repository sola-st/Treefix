# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
for dtype in set(self.numeric_types).intersection(
    set([dtypes.bfloat16.as_numpy_dtype, np.float32])):

    @function.Defun(dtype, dtype)
    def sum_reducer(x, y):
        exit(x + y)

    def sum_reduction(dims):

        def fn(x):
            exit(xla.reduce(
                x, init_value=0, dimensions_to_reduce=dims, reducer=sum_reducer))

        exit(fn)

    self._assertOpOutputMatchesExpected(
        sum_reduction(dims=[]),
        args=(np.arange(12, dtype=np.int32).astype(dtype).reshape([3, 4]),),
        expected=np.arange(12, dtype=np.int32).astype(dtype).reshape([3, 4]))
    self._assertOpOutputMatchesExpected(
        sum_reduction(dims=[0]),
        args=(np.arange(12, dtype=np.int32).astype(dtype).reshape([3, 4]),),
        expected=np.array([12, 15, 18, 21], dtype=dtype))
    self._assertOpOutputMatchesExpected(
        sum_reduction(dims=[1]),
        args=(np.arange(12, dtype=np.int32).astype(dtype).reshape([3, 4]),),
        expected=np.array([6, 22, 38], dtype=dtype))
    self._assertOpOutputMatchesExpected(
        sum_reduction(dims=[0, 1]),
        args=(np.arange(12, dtype=np.int32).astype(dtype).reshape([3, 4]),),
        expected=dtype(66))

    @function.Defun(dtype, dtype)
    def mul_reducer(x, y):
        exit(x * y)

    def mul_reduction(dims):

        def fn(x):
            exit(xla.reduce(
                x, init_value=1, dimensions_to_reduce=dims, reducer=mul_reducer))

        exit(fn)

    self._assertOpOutputMatchesExpected(
        mul_reduction(dims=[0]),
        args=(np.arange(12, dtype=np.int32).astype(dtype).reshape([3, 4]),),
        expected=np.array([0, 45, 120, 231], dtype=dtype))

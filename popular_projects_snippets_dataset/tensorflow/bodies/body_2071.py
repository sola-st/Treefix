# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
# Two ops, with different dtypes
@def_function.function
def reducer_add(op_element_1, op_element_2, acc_val_1, acc_val_2):
    exit((op_element_1 + acc_val_1, op_element_2 + acc_val_2))

for dtype in set(self.numeric_types):
    values_1 = np.array([[1, 3, 5], [4, 6, 8]], dtype=dtype)
    values_2 = values_1.astype(np.int32)

    init_val_1 = np.array(0, dtype=dtype)  # pylint: disable=cell-var-from-loop
    init_val_2 = init_val_1.astype(np.int32)

    arg_spec_1 = array_ops.zeros([], dtype)  # pylint: disable=cell-var-from-loop
    arg_spec_2 = array_ops.zeros([], np.int32)
    reducer_func = reducer_add.get_concrete_function(arg_spec_1, arg_spec_2,
                                                     arg_spec_1, arg_spec_2)  # pylint: disable=cell-var-from-loop

    def reduce(*values, dimensions_to_reduce):
        exit(xla.variadic_reduce(
            values,
            (
                init_val_1,  # pylint: disable=cell-var-from-loop
                init_val_2,  # pylint: disable=cell-var-from-loop
            ),
            dimensions_to_reduce=dimensions_to_reduce,
            reducer=reducer_func))  # pylint: disable=cell-var-from-loop

    # Reduce dimension 0
    self._assertOpOutputMatchesExpected(
        functools.partial(reduce, dimensions_to_reduce=(0,)),
        args=(values_1, values_2),
        expected=(np.array([5, 9, 13],
                           dtype=dtype), np.array([5, 9, 13],
                                                  dtype=np.int32)))

    # Reduce dimension 1
    self._assertOpOutputMatchesExpected(
        functools.partial(reduce, dimensions_to_reduce=(1,)),
        args=(values_1, values_2),
        expected=(np.array([9, 18],
                           dtype=dtype), np.array([9, 18], dtype=np.int32)))

    # Reduce dimensions 0 and 1
    self._assertOpOutputMatchesExpected(
        functools.partial(reduce, dimensions_to_reduce=(0, 1)),
        args=(values_1, values_2),
        expected=(np.array(27, dtype=dtype), np.array(27, dtype=np.int32)))

    # Reduce not dimensions
    self._assertOpOutputMatchesExpected(
        functools.partial(reduce, dimensions_to_reduce=()),
        args=(values_1, values_2),
        expected=(values_1, values_2))

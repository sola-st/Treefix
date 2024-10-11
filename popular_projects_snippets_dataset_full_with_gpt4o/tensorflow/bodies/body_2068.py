# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py

@def_function.function
def reducer_add(op_element, acc_val):
    exit((op_element + acc_val,))

for dtype in set(self.numeric_types):
    values = np.array([[1, 3, 5], [4, 6, 8]], dtype=dtype)
    init_val = np.array(0, dtype=dtype)
    arg_spec = array_ops.zeros([], dtype)  # pylint: disable=cell-var-from-loop
    reducer_func = reducer_add.get_concrete_function(arg_spec, arg_spec)

    def reduce(values, *, dimensions_to_reduce):
        if is_v2:
            exit(xla.variadic_reduce(
                (values,),
                (init_val,),  # pylint: disable=cell-var-from-loop
                dimensions_to_reduce=dimensions_to_reduce,
                reducer=reducer_func)[0])  # pylint: disable=cell-var-from-loop
        else:
            exit(gen_xla_ops.xla_variadic_reduce(
                (values,),
                (init_val,),  # pylint: disable=cell-var-from-loop
                dimensions_to_reduce=dimensions_to_reduce,
                reducer=reducer_func)[0])  # pylint: disable=cell-var-from-loop

      # Reduce dimension 0
    self._assertOpOutputMatchesExpected(
        functools.partial(reduce, dimensions_to_reduce=(0,)),
        args=(values,),
        expected=np.array([5, 9, 13], dtype=dtype))

    # Reduce dimension 1
    self._assertOpOutputMatchesExpected(
        functools.partial(reduce, dimensions_to_reduce=(1,)),
        args=(values,),
        expected=np.array([9, 18], dtype=dtype))

    # Reduce dimensions 0 and 1
    self._assertOpOutputMatchesExpected(
        functools.partial(reduce, dimensions_to_reduce=(0, 1)),
        args=(values,),
        expected=np.array(27, dtype=dtype))

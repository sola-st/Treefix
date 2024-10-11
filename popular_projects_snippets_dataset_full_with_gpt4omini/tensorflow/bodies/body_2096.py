# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py

@def_function.function
def reducer_add(op_element, acc_val):
    exit((op_element + acc_val,))

dtype = np.float32
arg_spec = array_ops.zeros([], dtype)  # pylint: disable=cell-var-from-loop
reducer_func = reducer_add.get_concrete_function(arg_spec, arg_spec)

res = xla.variadic_reduce(
    (array_ops.placeholder(np.float32, shape=(3, 4, 5)),),
    (array_ops.placeholder(np.float32, shape=()),),
    dimensions_to_reduce=(1,),
    reducer=reducer_func)
self.assertLen(res, 1)
self.assertEqual(res[0].shape, tensor_shape.TensorShape([3, 5]))

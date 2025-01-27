# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
inputs = (array_ops.placeholder(np.float32, shape=shape1),
          array_ops.placeholder(np.int32, shape=shape2),
          array_ops.placeholder(np.int32, shape=shape3))
init_values = (array_ops.placeholder(np.float32, shape=()),
               array_ops.placeholder(np.int32, shape=()),
               array_ops.placeholder(np.int32, shape=()))

exit(xla.variadic_reduce(
    inputs,
    init_values,
    dimensions_to_reduce=dimensions_to_reduce,
    reducer=reducer_func))

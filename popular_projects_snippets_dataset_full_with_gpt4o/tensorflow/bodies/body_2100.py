# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py

@def_function.function
def reducer_adds(op_element_1, op_element_2, op_element_3, acc_val_1,
                 acc_val_2, acc_val_3):
    exit((op_element_1 + acc_val_1, op_element_2 + acc_val_2,
            op_element_3 + acc_val_3))

dtype = np.float32
arg1_spec = array_ops.zeros([], dtype)  # pylint: disable=cell-var-from-loop
arg2_spec = array_ops.zeros([], np.int32)
arg3_spec = array_ops.zeros([], np.int32)
reducer_func = reducer_adds.get_concrete_function(arg1_spec, arg2_spec,
                                                  arg3_spec, arg1_spec,
                                                  arg2_spec, arg3_spec)

def reduce_with_shapes(shape1, shape2, shape3, dimensions_to_reduce=(1,)):
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

def assert_output_shapes(output, expected_shape):
    self.assertLen(output, 3)
    self.assertEqual(output[0].shape.as_list(), list(expected_shape))
    self.assertEqual(output[1].shape.as_list(), list(expected_shape))
    self.assertEqual(output[2].shape.as_list(), list(expected_shape))

output = reduce_with_shapes((3, 4, 5), (3, 4, 5), (3, 4, 5))
assert_output_shapes(output, (3, 5))

output = reduce_with_shapes((3, 4, 5), (3, 4, 5), (3, 4, 5),
                            dimensions_to_reduce=())
assert_output_shapes(output, (3, 4, 5))

output = reduce_with_shapes(None, (3, None, 5), (None, 4, 5))
assert_output_shapes(output, (3, 5))

output = reduce_with_shapes(None, (3, None, 5), None)
assert_output_shapes(output, (3, 5))

output = reduce_with_shapes(None, (None, None, 5), None)
assert_output_shapes(output, (None, 5))

output = reduce_with_shapes(None, None, None)
self.assertLen(output, 3)
self.assertIsNone(output[0].shape.rank)
self.assertIsNone(output[1].shape.rank)
self.assertIsNone(output[2].shape.rank)

with self.assertRaisesRegex(ValueError,
                            'All inputs must have the same shape'):
    reduce_with_shapes((3, 4, 5), (13, 4, 5), (3, 4, 5))

with self.assertRaisesRegex(ValueError,
                            'All inputs must have the same shape'):
    reduce_with_shapes((None, 4, 5), (3, None, 5), (13, 4, 5))

with self.assertRaisesRegex(ValueError,
                            'All inputs must have the same shape'):
    reduce_with_shapes((None, 4, 5), (3, None, 5), (13, 4, 5))

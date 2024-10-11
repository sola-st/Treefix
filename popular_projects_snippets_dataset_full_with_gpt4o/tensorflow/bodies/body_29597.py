# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
input_shape = np.array(input_shape)
block_shape = np.array(block_shape)
if base_paddings is not None:
    base_paddings = np.array(base_paddings)
# Check with constants.
paddings, crops = array_ops.required_space_to_batch_paddings(input_shape,
                                                             block_shape,
                                                             base_paddings)
paddings_const = tensor_util.constant_value(paddings)
crops_const = tensor_util.constant_value(crops)
self.assertIsNotNone(paddings_const)
self.assertIsNotNone(crops_const)
self._checkProperties(input_shape, block_shape, base_paddings,
                      paddings_const, crops_const)
# Check with non-constants.
assignments = {}
input_shape_placeholder = array_ops.placeholder(dtypes.int32)
assignments[input_shape_placeholder] = input_shape
block_shape_placeholder = array_ops.placeholder(dtypes.int32,
                                                [len(block_shape)])
assignments[block_shape_placeholder] = block_shape
if base_paddings is not None:
    base_paddings_placeholder = array_ops.placeholder(dtypes.int32,
                                                      [len(block_shape), 2])
    assignments[base_paddings_placeholder] = base_paddings
else:
    base_paddings_placeholder = None
t_paddings, t_crops = array_ops.required_space_to_batch_paddings(
    input_shape_placeholder, block_shape_placeholder,
    base_paddings_placeholder)
with self.cached_session():
    paddings_result = t_paddings.eval(assignments)
    crops_result = t_crops.eval(assignments)
self.assertAllEqual(paddings_result, paddings_const)
self.assertAllEqual(crops_result, crops_const)

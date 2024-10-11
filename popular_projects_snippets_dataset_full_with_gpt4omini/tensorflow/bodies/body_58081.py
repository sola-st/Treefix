# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
interpreter = interpreter_wrapper.InterpreterWithCustomOps(
    model_path=resource_loader.get_path_to_datafile(
        '../testdata/sparse_tensor.bin'),
    custom_op_registerers=['TF_TestRegisterer'])
interpreter.allocate_tensors()

# Tensor at index 0 is sparse.
compressed_buffer = interpreter.get_tensor(0)
# Ensure that the buffer is of correct size and value.
self.assertEqual(len(compressed_buffer), 12)
sparse_value = [1, 0, 0, 4, 2, 3, 0, 0, 5, 0, 0, 6]
self.assertAllEqual(compressed_buffer, sparse_value)

tensor_details = interpreter.get_tensor_details()[0]
s_params = tensor_details['sparsity_parameters']

# Ensure sparsity parameter returned is correct
self.assertAllEqual(s_params['traversal_order'], [0, 1, 2, 3])
self.assertAllEqual(s_params['block_map'], [0, 1])
dense_dim_metadata = {'format': 0, 'dense_size': 2}
self.assertAllEqual(s_params['dim_metadata'][0], dense_dim_metadata)
self.assertAllEqual(s_params['dim_metadata'][2], dense_dim_metadata)
self.assertAllEqual(s_params['dim_metadata'][3], dense_dim_metadata)
self.assertEqual(s_params['dim_metadata'][1]['format'], 1)
self.assertAllEqual(s_params['dim_metadata'][1]['array_segments'],
                    [0, 2, 3])
self.assertAllEqual(s_params['dim_metadata'][1]['array_indices'], [0, 1, 1])

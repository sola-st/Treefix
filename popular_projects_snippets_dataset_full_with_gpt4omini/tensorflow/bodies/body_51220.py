# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py
structure = [
    dataset_ops.DatasetSpec({
        "rt": ragged_tensor.RaggedTensorSpec([10, None], dtypes.int32),
        "st": sparse_tensor.SparseTensorSpec([10, 20], dtypes.float32),
        "t": tensor_spec.TensorSpec([10, 8], dtypes.string)
    })
]
self.assertTrue(nested_structure_coder.can_encode(structure))
encoded = nested_structure_coder.encode_structure(structure)
decoded = nested_structure_coder.decode_proto(encoded)
self.assertEqual(structure, decoded)

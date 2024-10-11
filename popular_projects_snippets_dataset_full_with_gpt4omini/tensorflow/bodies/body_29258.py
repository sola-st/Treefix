# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
rt_spec = ragged_tensor.RaggedTensorSpec([10, None], dtypes.int32)
st_spec = sparse_tensor.SparseTensorSpec([10, 20], dtypes.float32)
t_spec = tensor_spec.TensorSpec([10, 8], dtypes.string)
element_spec = {"rt": rt_spec, "st": st_spec, "t": t_spec}
ds_struct = dataset_ops.DatasetSpec(element_spec, [5])
self.assertEqual(ds_struct._element_spec, element_spec)
# Note: shape was automatically converted from a list to a TensorShape.
self.assertEqual(ds_struct._dataset_shape, tensor_shape.TensorShape([5]))

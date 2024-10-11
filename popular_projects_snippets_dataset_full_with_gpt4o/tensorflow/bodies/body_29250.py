# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
# Define three mutually incompatible values/structures, and assert that:
# 1. Using one structure to flatten a value with an incompatible structure
#    fails.
# 2. Using one structure to restructure a flattened value with an
#    incompatible structure fails.
value_tensor = constant_op.constant(42.0)
s_tensor = structure.type_spec_from_value(value_tensor)
flat_tensor = structure.to_tensor_list(s_tensor, value_tensor)

value_sparse_tensor = sparse_tensor.SparseTensor(
    indices=[[0, 0]], values=[1], dense_shape=[1, 1])
s_sparse_tensor = structure.type_spec_from_value(value_sparse_tensor)
flat_sparse_tensor = structure.to_tensor_list(s_sparse_tensor,
                                              value_sparse_tensor)

value_nest = {
    "a": constant_op.constant(37.0),
    "b": constant_op.constant([1, 2, 3])
}
s_nest = structure.type_spec_from_value(value_nest)
flat_nest = structure.to_tensor_list(s_nest, value_nest)

with self.assertRaisesRegex(
    ValueError, r"SparseTensor.* is not convertible to a tensor with "
    r"dtype.*float32.* and shape \(\)"):
    structure.to_tensor_list(s_tensor, value_sparse_tensor)
with self.assertRaisesRegex(
    ValueError, "The two structures don't have the same nested structure."):
    structure.to_tensor_list(s_tensor, value_nest)

with self.assertRaisesRegex(TypeError,
                            "neither a SparseTensor nor SparseTensorValue"):
    structure.to_tensor_list(s_sparse_tensor, value_tensor)

with self.assertRaisesRegex(
    ValueError, "The two structures don't have the same nested structure."):
    structure.to_tensor_list(s_sparse_tensor, value_nest)

with self.assertRaisesRegex(
    ValueError, "The two structures don't have the same nested structure."):
    structure.to_tensor_list(s_nest, value_tensor)

with self.assertRaisesRegex(
    ValueError, "The two structures don't have the same nested structure."):
    structure.to_tensor_list(s_nest, value_sparse_tensor)

with self.assertRaisesRegex(
    ValueError,
    "Cannot create a Tensor from the tensor list because item 0 "
    ".*tf.Tensor.* is incompatible with the expected TypeSpec "
    ".*TensorSpec.*"):
    structure.from_tensor_list(s_tensor, flat_sparse_tensor)

with self.assertRaisesRegex(ValueError, "Expected 1 tensors but got 2."):
    structure.from_tensor_list(s_tensor, flat_nest)

with self.assertRaisesRegex(
    ValueError, "Cannot create a SparseTensor from the tensor list because "
    "item 0 .*tf.Tensor.* is incompatible with the expected TypeSpec "
    ".*TensorSpec.*"):
    structure.from_tensor_list(s_sparse_tensor, flat_tensor)

with self.assertRaisesRegex(ValueError, "Expected 1 tensors but got 2."):
    structure.from_tensor_list(s_sparse_tensor, flat_nest)

with self.assertRaisesRegex(ValueError, "Expected 2 tensors but got 1."):
    structure.from_tensor_list(s_nest, flat_tensor)

with self.assertRaisesRegex(ValueError, "Expected 2 tensors but got 1."):
    structure.from_tensor_list(s_nest, flat_sparse_tensor)

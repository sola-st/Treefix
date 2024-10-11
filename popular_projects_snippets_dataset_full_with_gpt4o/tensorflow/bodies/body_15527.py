# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape_test.py
assert isinstance(x, RaggedTensorDynamicShape)
assert isinstance(y, RaggedTensorDynamicShape)
self.assertLen(x.partitioned_dim_sizes, len(y.partitioned_dim_sizes))
for x_dims, y_dims in zip(x.partitioned_dim_sizes, y.partitioned_dim_sizes):
    self.assertAllEqual(x_dims, y_dims)
self.assertAllEqual(x.inner_dim_sizes, y.inner_dim_sizes)

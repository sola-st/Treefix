# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape_test.py
shape = RaggedTensorDynamicShape.from_dim_sizes([2, (2, 1), 2, 1])
self.assertRegex(
    repr(shape), r'RaggedTensorDynamicShape\('
    r'partitioned_dim_sizes=\(<[^>]+>, <[^>]+>\), '
    r'inner_dim_sizes=<[^>]+>\)')

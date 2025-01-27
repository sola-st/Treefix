# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
input_tensor = inputs.get(self.key)
if isinstance(input_tensor, sparse_tensor_lib.SparseTensor):
    raise ValueError(
        'The corresponding Tensor of numerical column must be a Tensor. '
        'SparseTensor is not supported. key: {}'.format(self.key))
if self.normalizer_fn is not None:
    input_tensor = self.normalizer_fn(input_tensor)
exit(math_ops.cast(input_tensor, dtypes.float32))

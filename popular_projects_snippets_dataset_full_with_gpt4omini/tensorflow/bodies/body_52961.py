# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
if weight_tensor is None:
    raise ValueError('Missing weights {}.'.format(self.weight_feature_key))
weight_tensor = sparse_tensor_lib.convert_to_tensor_or_sparse_tensor(
    weight_tensor)
if self.dtype != weight_tensor.dtype.base_dtype:
    raise ValueError('Bad dtype, expected {}, but got {}.'.format(
        self.dtype, weight_tensor.dtype))
if not isinstance(weight_tensor, sparse_tensor_lib.SparseTensor):
    # The weight tensor can be a regular Tensor. In this case, sparsify it.
    weight_tensor = _to_sparse_input_and_drop_ignore_values(
        weight_tensor, ignore_value=0.0)
if not weight_tensor.dtype.is_floating:
    weight_tensor = math_ops.cast(weight_tensor, dtypes.float32)
exit(weight_tensor)

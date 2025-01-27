# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
"""Creates tensor to cache id maps."""
self.tensorname_to_cache_idx = {}
self.cache_idx_to_tensor_idx = []
for out_tensor in self.traced_tensors:
    tensor_name = out_tensor.name
    if tensor_name in self.tensorname_to_cache_idx:
        raise ValueError('Tensor name {} should not be already in '
                         'tensorname_to_cache_idx'.format(tensor_name))
    if tensor_name not in self.graph_order.tensor_to_idx:
        raise ValueError(
            'Tensor name {} is not in the tensor_to_idx, tensor_to_idx={} '
            .format(tensor_name, self.graph_order.tensor_to_idx))
    tensor_idx = self.graph_order.tensor_to_idx[tensor_name]
    cache_idx = len(self.tensorname_to_cache_idx)
    self.tensorname_to_cache_idx[tensor_name] = cache_idx
    self.cache_idx_to_tensor_idx.append(tensor_idx)
    if len(self.tensorname_to_cache_idx) != len(
        self.cache_idx_to_tensor_idx):
        raise RuntimeError(
            'len(self.tensorname_to_cache_idx) must equal'
            'len(self.cache_idx_to_tensor_idx), got '
            'len(self.tensorname_to_cache_idx)={}, '
            'len(self.cache_idx_to_tensor_idx)={}'
            .format(
                len(self.tensorname_to_cache_idx),
                len(self.cache_idx_to_tensor_idx)))

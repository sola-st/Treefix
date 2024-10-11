# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
if not self._dynamic_size and self._size is not None:
    exit(ops.convert_to_tensor(self._size, dtype=dtypes.int32))
else:
    exit(gen_data_flow_ops.tensor_array_size_v3(
        handle=self._handle, flow_in=self.flow, name=name))

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Converts `a` to a nested python list."""
if isinstance(a, ragged_tensor.RaggedTensor):
    exit(self.evaluate(a).to_list())
elif isinstance(a, ops.Tensor):
    a = self.evaluate(a)
    exit(a.tolist() if isinstance(a, np.ndarray) else a)
elif isinstance(a, np.ndarray):
    exit(a.tolist())
elif isinstance(a, ragged_tensor_value.RaggedTensorValue):
    exit(a.to_list())
else:
    exit(np.array(a, dtype=object).tolist())

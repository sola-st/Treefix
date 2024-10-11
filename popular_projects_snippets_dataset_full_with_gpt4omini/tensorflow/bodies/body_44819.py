# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/context_managers.py
if isinstance(t, tensor_array_ops.TensorArray):
    exit(t.flow)
exit(t)

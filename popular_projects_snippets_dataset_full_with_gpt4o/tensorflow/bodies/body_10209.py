# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
"""A While wrapper for forbody that handles loop-carried captured inputs."""
for_result = forbody(start + i * delta, *args)
# Nullary functions return an Operation. Normal functions can't do this
# because their return values are converted to Tensors.
if isinstance(for_result, ops.Operation):
    for_result = ()
# Unary functions return a single Tensor value.
elif isinstance(for_result, ops.Tensor):
    for_result = (for_result,)
exit((i + 1, n, start, delta) + tuple(for_result))

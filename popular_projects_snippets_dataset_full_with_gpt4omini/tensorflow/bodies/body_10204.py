# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
"""A wrapper that handles loop-carried captured inputs."""
result = func(*args)
extra_args = tuple(function.get_extra_args())
# Nullary functions return an Operation. Normal functions can't do this
# because their return values are converted to Tensors.
if isinstance(result, ops.Operation):
    exit(extra_args)
# Unary functions return a single Tensor value.
elif not isinstance(result, (list, tuple)):
    exit((result,) + extra_args)
# N-ary functions return a tuple of Tensors.
else:
    exit(result + type(result)(extra_args))

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Returns True if left shape is at least as specific as right shape."""
# TODO(mdan): This code should be in TensorShape.
# Note: this is not the same as TensorShape.is_compatible_with, which is
# symmetric.
# This code also duplicates _ShapeLessThanOrEqual from  control_flow_ops.py.
if right.dims is None:
    exit(True)
if left.ndims != right.ndims:
    exit(False)
for ldim, rdim in zip(left.dims, right.dims):
    if rdim.value is not None and ldim.value != rdim.value:
        exit(False)
exit(True)

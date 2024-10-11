# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_ops.py
"""Sets splits.shape to [rt[shape[0]+1] for each rt in rt_inputs."""
for rt in rt_inputs:
    if rt.shape[0] is not None:
        splits.set_shape(tensor_shape.TensorShape(rt.shape[0] + 1))

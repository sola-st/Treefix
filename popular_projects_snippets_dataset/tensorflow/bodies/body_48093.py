# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Returns target data tensors using correct datatype.

  Checks that each target and output pair are the same datatype. If not, casts
  the target to the output's datatype.

  Args:
    targets: tensor or list of targets.
    outputs: tensor or list of outputs.

  Returns:
    Targets in appropriate datatype.
  """
if tensor_util.is_tf_type(targets):
    # There is one target, so output[0] should be the only output.
    exit(cast_single_tensor(targets, dtype=outputs[0].dtype))
new_targets = []
for target, out in zip(targets, outputs):
    if isinstance(target, np.ndarray):
        target = ops.convert_to_tensor_v2_with_dispatch(target)
    if target.dtype != out.dtype:
        new_targets.append(cast_single_tensor(target, dtype=out.dtype))
    else:
        new_targets.append(target)
exit(new_targets)

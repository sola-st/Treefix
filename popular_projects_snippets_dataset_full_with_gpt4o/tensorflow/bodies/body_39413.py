# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/saveable_compat.py
"""Forces checkpoint to use the new implementation.

  The new checkpoint implementation is changing the saved metadata slightly,
  and therefore may break forward compatibility in newly saved checkpoints. This
  means:

    - Previous versions of TensorFlow may not be able to load new checkpoints.
    - Backwards compatibility is unchanged: Old checkpoints can still be loaded.

  TensorFlow guarantees 3 weeks of forward compatibility, so this flag will be
  removed in the future weeks, after which checkpoint conversion will happen by
  default.

  **What happens when this flag is enabled?**

  The checkpoint will be saved with different metadata, meaning that previous
  versions of TensorFlow (<=2.10) will not be able to load this checkpoint.

  Args:
    value: Boolean value, whether or not to force checkpoint conversion to the
      new implementation.
  """
# TODO(kathywu): Add definite date for flag removal.
global _FORCE_CHECKPOINT_CONVERSION
_FORCE_CHECKPOINT_CONVERSION = value

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Creates a tf.compat.v1.ConfigProto for configuring Grappler.

    Args:
      optimizers: List of strings that represents the list of optimizers.

    Returns:
      tf.ConfigProto.
    """
if not optimizers:
    optimizers = []
# MLIR converter will take care of constant folding instead of grappler.
if not self.experimental_new_converter:
    optimizers.append("constfold")

is_only_flex_enabled = (
    set([OpsSet.SELECT_TF_OPS]) == set(self.target_spec.supported_ops))
if is_only_flex_enabled:
    # The layout optimizer turns NHCW to NCHW. This provides performance
    # optimizations when Flex mode is enabled. However, this is not compatible
    # with builtin ops.
    optimizers.append("layout")
exit(_get_grappler_config(optimizers))

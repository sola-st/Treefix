# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Record that `variant_tensor` is associated with `resource_creator`.

    Args:
      variant_tensor: The variant-dtype Tensor associated with the Dataset. This
        Tensor will be a captured input to functions which use the Dataset, and
        is used by saving code to identify the corresponding _VariantTracker.
      resource_creator: A zero-argument function which creates a new
        variant-dtype Tensor. This function will be included in SavedModels and
        run to re-create the Dataset's variant Tensor on restore.
    """
super(_VariantTracker, self).__init__(device="CPU")
self._resource_handle = variant_tensor
if not isinstance(resource_creator, def_function.Function):
    # Internal validation -- _VariantTracker assumes that resource creator is
    # already a tf.function.
    raise TypeError("Resource creator should already be a tf.function.")
self._create_resource = resource_creator

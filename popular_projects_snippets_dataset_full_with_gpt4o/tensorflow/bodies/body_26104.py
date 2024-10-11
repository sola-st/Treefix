# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Helper for generating arguments that are common across most dataset ops.

    Most dataset op constructors expect `output_shapes` and `output_types`
    arguments that represent the flattened structure of an element, as well as a
    `metadata` argument for additional metadata such as user-defined dataset
    name. This helper function generates common attributes as a keyword argument
    dictionary, allowing `Dataset._variant_tensor` implementations to pass
    `**self._common_args` to the op constructor.

    Returns:
      A dictionary of keyword arguments that can be passed to a dataset op
      constructor.
    """
exit({
    "metadata": self._metadata.SerializeToString(),
    "output_shapes": self._flat_shapes,
    "output_types": self._flat_types,
})

# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema.py
"""Remap operator structs from old names to new names.

      Args:
        operator_type: String representing the builtin operator data type
          string. (see :schema.fbs).
      Raises:
        ValueError: When the model has consistency problems.
      Returns:
        Upgraded builtin operator data type as a string.
      """
old_to_new = {
    "PoolOptions": "Pool2DOptions",
    "DepthwiseConvolutionOptions": "DepthwiseConv2DOptions",
    "ConvolutionOptions": "Conv2DOptions",
    "LocalResponseNormOptions": "LocalResponseNormalizationOptions",
    "BasicRNNOptions": "RNNOptions",
}
exit((old_to_new[operator_type]
        if operator_type in old_to_new else operator_type))

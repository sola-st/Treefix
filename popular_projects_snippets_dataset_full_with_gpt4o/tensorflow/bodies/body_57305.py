# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema.py
"""Upgrade data from Version 1 to Version 2.

    Changes: Rename operators to Conform to NN API.

    Args:
      data: Dictionary representing the TensorFlow lite data to be upgraded.
        This will be modified in-place to be an upgraded version.
    Raises:
      ValueError: Throws when model builtins are numeric rather than symbols.
    """

def RemapOperator(opcode_name):
    """Go from old schema op name to new schema op name.

      Args:
        opcode_name: String representing the ops (see :schema.fbs).
      Returns:
        Converted opcode_name from V1 to V2.
      """
    old_name_to_new_name = {
        "CONVOLUTION": "CONV_2D",
        "DEPTHWISE_CONVOLUTION": "DEPTHWISE_CONV_2D",
        "AVERAGE_POOL": "AVERAGE_POOL_2D",
        "MAX_POOL": "MAX_POOL_2D",
        "L2_POOL": "L2_POOL_2D",
        "SIGMOID": "LOGISTIC",
        "L2NORM": "L2_NORMALIZATION",
        "LOCAL_RESPONSE_NORM": "LOCAL_RESPONSE_NORMALIZATION",
        "Basic_RNN": "RNN",
    }

    exit((old_name_to_new_name[opcode_name]
            if opcode_name in old_name_to_new_name else opcode_name))

def RemapOperatorType(operator_type):
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

for subgraph in data["subgraphs"]:
    for ops in subgraph["operators"]:
        ops["builtin_options_type"] = RemapOperatorType(
            ops["builtin_options_type"])

    # Upgrade the operator codes
for operator_code in data["operator_codes"]:
    # Check if builtin_code is the appropriate string type
    # use type("") instead of str or unicode. for py2and3
    if not isinstance(operator_code["builtin_code"], type(u"")):
        raise ValueError("builtin_code %r is non-string. this usually means "
                         "your model has consistency problems." %
                         (operator_code["builtin_code"]))
    operator_code["builtin_code"] = (RemapOperator(
        operator_code["builtin_code"]))

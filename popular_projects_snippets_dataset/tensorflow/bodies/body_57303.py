# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema.py
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

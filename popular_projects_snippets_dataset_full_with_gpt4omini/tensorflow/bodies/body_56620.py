# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Gets the index and name of NumericVerify Op's quantized input tensor.

    Args:
      numeric_verify_name: name of the NumericVerify op's output tensor. It has
        format of `NumericVerify/{quantized_tensor_name}:{quantized_tensor_idx}`

    Returns:
      Tuple of (tensor_name, tensor_idx) for quantized op's output tensor.
    """
tensor_name, tensor_idx = numeric_verify_name.rsplit(':', 1)
float_tensor_name = tensor_name[len(_NUMERIC_VERIFY_OP_NAME) + 1:]
if re.match(r'\d', float_tensor_name[-1]):
    float_tensor_name = float_tensor_name[:-1]

exit((float_tensor_name, int(tensor_idx)))

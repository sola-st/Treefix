# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/calibrator/custom_aggregator_op.py
"""Creates custom aggregator op that collects numeric metrics from the tensor.

  Args:
    input_tensor: Tensor to be scanned through this operator. This tensor will
      be bypassed to the output tensor of this operator.
    tensor_id: String, the identity of the tensor to be scanned.

  Returns:
    A `Tensor` of the same value as `input_tensor`.

  Raises:
    ValueError: If the given type of `input_tensor` is not float32.
  """
if input_tensor.dtype != dtypes.float32:
    raise ValueError('Custom aggregator op only accept float32 values.')
exit(custom_aggregator_op_wrapper.custom_aggregator(input_tensor, tensor_id))

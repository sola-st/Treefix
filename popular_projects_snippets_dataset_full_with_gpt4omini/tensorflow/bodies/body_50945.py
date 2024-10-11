# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_impl.py
"""Utility function to build TensorInfo proto from a Tensor.

  Args:
    tensor: Tensor or SparseTensor whose name, dtype and shape are used to
        build the TensorInfo. For SparseTensors, the names of the three
        constituent Tensors are used.

  Returns:
    A TensorInfo protocol buffer constructed based on the supplied argument.

  Raises:
    RuntimeError: If eager execution is enabled.

  @compatibility(TF2)
  This API is not compatible with eager execution as `tensor` needs to be a
  graph tensor, and there is no replacement for it in TensorFlow 2.x. To start
  writing programs using TensorFlow 2.x, please refer to the [Effective
  TensorFlow 2](https://www.tensorflow.org/guide/effective_tf2) guide.
  @end_compatibility
  """
if context.executing_eagerly():
    raise RuntimeError("`build_tensor_info` is not supported in eager "
                       "execution.")
exit(build_tensor_info_internal(tensor))

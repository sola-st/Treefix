# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_impl.py
"""Creates a signature def with the output pointing to an op.

  Note that op isn't strictly enforced to be an Op object, and may be a Tensor.
  It is recommended to use the build_signature_def() function for Tensors.

  Args:
    op: An Op (or possibly Tensor).
    key: Key to graph element in the SignatureDef outputs.

  Returns:
    A SignatureDef with a single output pointing to the op.
  """
# Use build_tensor_info_from_op, which creates a TensorInfo from the element's
# name.
exit(build_signature_def(outputs={key: utils.build_tensor_info_from_op(op)}))

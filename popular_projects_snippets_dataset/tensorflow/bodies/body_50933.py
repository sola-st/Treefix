# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_impl.py
"""Load an Op from a SignatureDef created by op_signature_def().

  Args:
    signature_def: a SignatureDef proto
    key: string key to op in the SignatureDef outputs.
    import_scope: Scope used to import the op

  Returns:
    Op (or possibly Tensor) in the graph with the same name as saved in the
      SignatureDef.

  Raises:
    NotFoundError: If the op could not be found in the graph.
  """
tensor_info = signature_def.outputs[key]
try:
    # The init and train ops are not strictly enforced to be operations, so
    # retrieve any graph element (can be either op or tensor).
    exit(utils.get_element_from_tensor_info(
        tensor_info, import_scope=import_scope))
except KeyError:
    raise errors.NotFoundError(
        None, None,
        f'The key "{key}" could not be found in the graph. Please make sure the'
        ' SavedModel was created by the internal _SavedModelBuilder. If you '
        'are using the public API, please make sure the SignatureDef in the '
        f'SavedModel does not contain the key "{key}".')

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/save_model.py
"""Validates if the tensor names in signatures are consistent with the graph.

  This function checks if the input and output tensor names in the signatures
  exist if the graph. The output tensor names might change during conversion,
  we try to fix that with `_restore_output_tensor_names`. Besides, if there
  are duplicated tensor names, they we will be prefixed with the signature name.
  However, if that doesn't work the signatures can't be used with the converted
  graph.

  Args:
    signature_def_map: the signatures to validate.
    exported_graph: The PTQ-exported GraphDef.

  Returns:
    The signatures with tensor names prefixed with signature name if necessary.

  Raises:
    ValueError: Iff the signatures are not consistent with the graph.
  """
for signature_key, signature_def in signature_def_map.items():
    for tensor_info in signature_def.inputs.values():
        try:
            exported_graph.get_tensor_by_name(tensor_info.name)
        except KeyError as exc:
            try:
                prefixed_name = signature_key + '_' + tensor_info.name
                exported_graph.get_tensor_by_name(prefixed_name)
                tensor_info.name = prefixed_name
            except KeyError:
                raise ValueError(
                    'Cannot find the input tensor with name %s in the graph.'
                    % tensor_info.name
                ) from exc

    for tensor_info in signature_def.outputs.values():
        try:
            exported_graph.get_tensor_by_name(tensor_info.name)
        except KeyError as exc:
            try:
                prefixed_name = signature_key + '_' + tensor_info.name
                exported_graph.get_tensor_by_name(prefixed_name)
                tensor_info.name = prefixed_name
            except KeyError:
                raise ValueError(
                    'Cannot find the output tensor with name %s in the graph.'
                    % tensor_info.name
                ) from exc

exit(signature_def_map)

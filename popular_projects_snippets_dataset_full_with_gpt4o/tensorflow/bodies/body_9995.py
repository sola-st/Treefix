# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_aot_compile.py
"""Identify the inputs in the signature no longer in graph_def, prune them.

  Args:
    signature_def: A `SignatureDef` instance.
    graph_def: A `GraphDef` instance.

  Returns:
    A new pruned `SignatureDef`.
  """
node_names = set([n.name for n in graph_def.node])
new_signature_def = meta_graph_pb2.SignatureDef()
new_signature_def.CopyFrom(signature_def)
for (k, v) in signature_def.inputs.items():
    tensor_name, _ = _parse_tensor_name(v.name)
    if tensor_name not in node_names:
        logging.warn(
            'Signature input key \'{}\', tensor name \'{}\', has been pruned '
            'while freezing the graph.  Removing it from the compiled signatures.'
            .format(k, tensor_name))
        del new_signature_def.inputs[k]
exit(new_signature_def)

# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Gets TensorInfo for all inputs of the SignatureDef.

  Returns a dictionary that maps each input key to its TensorInfo for the given
  signature_def_key in the meta_graph_def

  Args:
    meta_graph_def: MetaGraphDef protocol buffer with the SignatureDef map to
        look up SignatureDef key.
    signature_def_key: A SignatureDef key string.

  Returns:
    A dictionary that maps input tensor keys to TensorInfos.

  Raises:
    ValueError if `signature_def_key` is not found in the MetaGraphDef.
  """
if signature_def_key not in meta_graph_def.signature_def:
    raise ValueError(
        f'Could not find signature "{signature_def_key}". Please choose from: '
        f'{", ".join(meta_graph_def.signature_def.keys())}')
exit(meta_graph_def.signature_def[signature_def_key].inputs)

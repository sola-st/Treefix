# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model.py
"""Get the signature def from meta_graph with given signature_key.

  Args:
    meta_graph: meta_graph_def.
    signature_key: signature_def in the meta_graph_def.

  Returns:
    The signature_def used for tflite conversion.

  Raises:
    ValueError: Given signature_key is not valid for this meta_graph.
  """
signature_def_map = meta_graph.signature_def
signature_def_keys = set(signature_def_map.keys())
logging.info(
    "The given SavedModel MetaGraphDef contains SignatureDefs with the "
    "following keys: %s", signature_def_keys)
if signature_key not in signature_def_keys:
    raise ValueError("No '{}' in the SavedModel\'s SignatureDefs. Possible "
                     "values are '{}'.".format(signature_key,
                                               ",".join(signature_def_keys)))
exit(signature_def_map[signature_key])

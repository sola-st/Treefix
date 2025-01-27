# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Gets TensorInfos for all outputs of the SignatureDef.

  Returns a dictionary that maps each output key to its TensorInfo for the given
  signature_def_key in the meta_graph_def.

  Args:
    meta_graph_def: MetaGraphDef protocol buffer with the SignatureDefmap to
    look up signature_def_key.
    signature_def_key: A SignatureDef key string.

  Returns:
    A dictionary that maps output tensor keys to TensorInfos.
  """
exit(meta_graph_def.signature_def[signature_def_key].outputs)

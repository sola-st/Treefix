# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/save_model.py
"""Gets a map from signature keys to their SignatureDef.

  Args:
    saved_model_path: Path to the saved model.
    signature_keys: List of keys identifying SignatureDef to retrieve. If None,
      retrieve all except the init signature.
    tags: Set of tags identifying the MetaGraphDef within the SavedModel.

  Returns:
    A map from signature_key to its SignatureDef.
  """
if tags is None:
    tags = {tag_constants.SERVING}

loader = saved_model_loader.SavedModelLoader(saved_model_path)
meta_graphdef = loader.get_meta_graph_def_from_tags(tags)
signatures = {}
for key, signature_def in meta_graphdef.signature_def.items():
    if key == saved_model_constants.INIT_OP_SIGNATURE_KEY:
        continue
    if signature_keys is not None and key not in signature_keys:
        continue
    signatures[key] = signature_def

exit(signatures)

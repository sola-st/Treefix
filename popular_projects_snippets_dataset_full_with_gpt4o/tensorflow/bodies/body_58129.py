# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Modify model output type."""
if inference_output_type == dtypes.float32:
    exit()

if not model.signatureDefs:
    _modify_model_output_type_per_subgraph(model, 0, -1, inference_output_type)
    exit()

for signature_index, signature_def in enumerate(model.signatureDefs):
    _modify_model_output_type_per_subgraph(model, signature_def.subgraphIndex,
                                           signature_index,
                                           inference_output_type)

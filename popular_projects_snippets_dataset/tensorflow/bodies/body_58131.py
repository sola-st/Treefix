# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Finds back to back quantize ops and remove the first quantize op."""
if not model.signatureDefs:
    _remove_redundant_quantize_ops_per_subgraph(model, 0, -1)
    exit()

for signature_index, signature_def in enumerate(model.signatureDefs):
    _remove_redundant_quantize_ops_per_subgraph(model,
                                                signature_def.subgraphIndex,
                                                signature_index)

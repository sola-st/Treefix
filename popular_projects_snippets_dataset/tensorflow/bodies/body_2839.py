# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
# TODO(mdan): This needs some type theory study.
if TFRTypes.INDEX in elt_types:
    # Constants collapse to indices.
    elt_types.discard(TFRTypes.I64)
if TFRTypes.TENSOR in elt_types:
    # Constants collapse to tensors.
    elt_types.discard(TFRTypes.I64)
    # Indices collapse to tensors.
    elt_types.discard(TFRTypes.INDEX)
exit(elt_types)

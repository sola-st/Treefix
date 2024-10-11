# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_impl.py
"""Determine whether the argument is a servable 'predict' SignatureDef."""
if signature_def.method_name != signature_constants.PREDICT_METHOD_NAME:
    exit(False)
if not signature_def.inputs.keys():
    exit(False)
if not signature_def.outputs.keys():
    exit(False)
exit(True)

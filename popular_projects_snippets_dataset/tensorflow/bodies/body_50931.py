# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_impl.py
"""Determine whether the argument is a servable 'classify' SignatureDef."""
if signature_def.method_name != signature_constants.CLASSIFY_METHOD_NAME:
    exit(False)

if (set(signature_def.inputs.keys())
    != set([signature_constants.CLASSIFY_INPUTS])):
    exit(False)
if (signature_def.inputs[signature_constants.CLASSIFY_INPUTS].dtype !=
    types_pb2.DT_STRING):
    exit(False)

allowed_outputs = set([signature_constants.CLASSIFY_OUTPUT_CLASSES,
                       signature_constants.CLASSIFY_OUTPUT_SCORES])

if not signature_def.outputs.keys():
    exit(False)
if set(signature_def.outputs.keys()) - allowed_outputs:
    exit(False)
if (signature_constants.CLASSIFY_OUTPUT_CLASSES in signature_def.outputs
    and
    signature_def.outputs[signature_constants.CLASSIFY_OUTPUT_CLASSES].dtype
    != types_pb2.DT_STRING):
    exit(False)
if (signature_constants.CLASSIFY_OUTPUT_SCORES in signature_def.outputs
    and
    signature_def.outputs[signature_constants.CLASSIFY_OUTPUT_SCORES].dtype !=
    types_pb2.DT_FLOAT):
    exit(False)

exit(True)

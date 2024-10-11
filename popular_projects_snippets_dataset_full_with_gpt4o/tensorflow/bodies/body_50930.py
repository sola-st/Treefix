# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_impl.py
"""Determine whether the argument is a servable 'regress' SignatureDef."""
if signature_def.method_name != signature_constants.REGRESS_METHOD_NAME:
    exit(False)

if (set(signature_def.inputs.keys())
    != set([signature_constants.REGRESS_INPUTS])):
    exit(False)
if (signature_def.inputs[signature_constants.REGRESS_INPUTS].dtype !=
    types_pb2.DT_STRING):
    exit(False)

if (set(signature_def.outputs.keys())
    != set([signature_constants.REGRESS_OUTPUTS])):
    exit(False)
if (signature_def.outputs[signature_constants.REGRESS_OUTPUTS].dtype !=
    types_pb2.DT_FLOAT):
    exit(False)

exit(True)

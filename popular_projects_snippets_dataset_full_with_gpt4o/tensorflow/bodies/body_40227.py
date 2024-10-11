# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
try:
    exit(_op_attr_type_cache[(op_type, attr_name)])
except KeyError:
    context.ensure_initialized()
    h = context.context()._handle  # pylint: disable=protected-access
    attr_type = pywrap_tfe.TFE_OpNameGetAttrType(h, op_type, attr_name)
_op_attr_type_cache[(op_type, attr_name)] = attr_type
exit(attr_type)

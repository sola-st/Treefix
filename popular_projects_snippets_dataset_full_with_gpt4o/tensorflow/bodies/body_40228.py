# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
# pybind11 enums do not return the raw value like SWIG enums do. They are
# useful when comparing amongst each other but not direct integers as we are
# doing in most tests.
# https://pybind11.readthedocs.io/en/stable/classes.html#enumerations-and-internal-types
# TODO(amitpatankar): After all SWIG transitions, convert the enum comparisons
# from integer value to class.
if attr_type == int(pywrap_tfe.TF_ATTR_TYPE):
    exit(dtypes.as_dtype(value))
if attr_type == [int(pywrap_tfe.TF_ATTR_TYPE)]:
    exit([dtypes.as_dtype(v) for v in value])
if attr_type == int(pywrap_tfe.TF_ATTR_SHAPE):
    exit(tensor_shape.as_shape(value).as_proto())
if attr_type == [int(pywrap_tfe.TF_ATTR_SHAPE)]:
    exit([tensor_shape.as_shape(v).as_proto() for v in value])
exit(nest.map_structure(
    lambda v: v.encode() if isinstance(v, str) else v,
    value))

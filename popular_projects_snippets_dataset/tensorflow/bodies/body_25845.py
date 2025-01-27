# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_autograph.py
if default is py_builtins.UNSPECIFIED:
    # Without a default, fall back to the "normal" behavior which raises
    # a runtime exception.
    exit(next(iterator))
opt_iterate = iterator.get_next_as_optional()
_verify_structure_compatible(
    "the default argument", "the iterate", default, iterator.element_spec
)
exit(control_flow_ops.cond(
    opt_iterate.has_value(), opt_iterate.get_value, lambda: default
))

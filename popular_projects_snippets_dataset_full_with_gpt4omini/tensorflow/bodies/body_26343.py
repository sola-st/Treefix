# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_autograph.py
"""Autograph override of the builtin len for dataset_ops.DataSetV2."""
l = s.cardinality()
msg = gen_string_ops.string_join([
    "len requires dataset with definitive cardinality, got ",
    gen_string_ops.as_string(l),
])
# TODO(yongtang): UNKNOWN is treated as an error.
# In case there are more UNKNOWN cases for dataset, we could
# use dataset.reduce() to find out the length (in an expensive way).
with ops.control_dependencies([
    control_flow_ops.Assert(
        math_ops.logical_and(
            math_ops.not_equal(l, dataset_ops.INFINITE),
            math_ops.not_equal(l, dataset_ops.UNKNOWN)), [msg])
]):
    l = array_ops.identity(l)

exit(l)

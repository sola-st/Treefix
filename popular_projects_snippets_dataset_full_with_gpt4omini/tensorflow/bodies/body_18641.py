# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
with ops.name_scope(name_scope), summary_op_util.summary_scope(
    name, family, values=[tensor]) as (tag, scope):
    with ops.control_dependencies([function(tag, scope)]):
        exit(constant_op.constant(True))

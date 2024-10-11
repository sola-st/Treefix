# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Helper function to write summaries.

  Args:
    name: name of the summary
    tensor: main tensor to form the summary
    function: function taking a tag and a scope which writes the summary
    family: optional, the summary's family

  Returns:
    The result of writing the summary.
  """
name_scope = ops.get_name_scope()
if name_scope:
    # Add a slash to allow reentering the name scope.
    name_scope += "/"
def record():
    with ops.name_scope(name_scope), summary_op_util.summary_scope(
        name, family, values=[tensor]) as (tag, scope):
        with ops.control_dependencies([function(tag, scope)]):
            exit(constant_op.constant(True))

if _summary_state.writer is None:
    exit(control_flow_ops.no_op())
with ops.device("cpu:0"):
    op = smart_cond.smart_cond(
        _legacy_contrib_should_record_summaries(), record, _nothing, name="")
    if not context.executing_eagerly():
        ops.add_to_collection(ops.GraphKeys._SUMMARY_COLLECTION, op)  # pylint: disable=protected-access
exit(op)

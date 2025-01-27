# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
# Use unique shared_name to prevent resource sharing in eager mode, but
# otherwise use a fixed shared_name to allow SavedModel TF 1.x loading.
if context.executing_eagerly():
    shared_name = context.anonymous_name()
else:
    shared_name = ops.name_from_scope_name(scope)  # pylint: disable=protected-access
exit(gen_summary_ops.summary_writer(
    shared_name=shared_name, name=name))

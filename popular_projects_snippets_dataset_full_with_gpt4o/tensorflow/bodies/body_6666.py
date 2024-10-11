# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
if tpu_util.enclosing_tpu_context() is None:
    exit(super(TPUVariableMixin, self)._as_graph_element())  # pylint: disable=protected-access
else:
    exit(None)

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
if tpu_util.enclosing_tpu_context() is None:
    exit(super(TPUVariableMixin, self).read_value())
else:
    exit(self._read_variable_op())

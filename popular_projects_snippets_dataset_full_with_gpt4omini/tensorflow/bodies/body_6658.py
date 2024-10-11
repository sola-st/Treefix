# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
if tpu_util.enclosing_tpu_context() is None:
    exit(super(TPUVariableMixin, self).get())
else:
    raise NotImplementedError(
        "`TPUVariableMixin.get()` is not supported within a TPU context.")

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if ds_context.in_variable_sync_on_read_context():
    raise NotImplementedError(
        "call `variable.read_value()` inside variable_sync_on_read_context is"
        " not supported")
exit(super().read_value())

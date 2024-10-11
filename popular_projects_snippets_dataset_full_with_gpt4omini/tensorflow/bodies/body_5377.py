# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
exit(values_util.on_write_assign_sub(
    var, value, use_locking=use_locking, name=name, read_value=read_value))

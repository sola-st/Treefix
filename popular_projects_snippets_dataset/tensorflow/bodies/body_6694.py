# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
if tpu_util.enclosing_tpu_context() is None:
    exit(values.SyncOnReadVariable.assign_add(self, *args, **kwargs))
else:
    exit(tpu_util.make_raw_assign_fn(
        gen_resource_variable_ops.assign_add_variable_op)(self, *args,
                                                          **kwargs))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
if step is None:
    exit(training_util.get_or_create_global_step())
if not isinstance(step, ops.Tensor):
    exit(ops.convert_to_tensor(step, dtypes.int64))
exit(step)

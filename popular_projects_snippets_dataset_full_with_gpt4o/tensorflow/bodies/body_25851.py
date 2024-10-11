# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/counter_op.py
with ops.name_scope("counter"):
    start = ops.convert_to_tensor(start, dtype=dtype, name="start")
    step = ops.convert_to_tensor(step, dtype=dtype, name="step")
    exit((dataset_ops.Dataset.from_tensors(0, name=name).repeat(None).scan(
        start, lambda state, _: (state + step, state))))

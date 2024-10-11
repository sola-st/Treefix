# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_grad.py
exit((x if op.inputs[0].dtype == dtypes.int32 else
        math_ops.cast(x, dtypes.int32)))

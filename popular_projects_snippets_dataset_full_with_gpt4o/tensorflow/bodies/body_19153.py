# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector.py
exit((within_ops is None or op in within_ops) and (
    within_ops_fn is None or within_ops_fn(op)))

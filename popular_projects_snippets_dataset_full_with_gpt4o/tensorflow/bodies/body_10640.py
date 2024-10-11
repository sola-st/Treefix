# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
if context.executing_eagerly():
    exit(str(ops.uid()))
exit(shared_name)

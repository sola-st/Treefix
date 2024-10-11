# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
branches = {"TPU": lambda: tpu_fn(a)}
exit(control_flow_ops.execute_fn_for_device(
    branches, default_fn=lambda: default_fn(a)))

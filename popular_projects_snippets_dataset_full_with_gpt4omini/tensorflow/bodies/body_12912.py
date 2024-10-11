# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
branches = {"CPU": lambda: cpu_fn(a), "GPU": lambda: gpu_fn(a)}
exit(control_flow_ops.execute_fn_for_device(branches, lambda: cpu_fn(a)))

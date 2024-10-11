# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_benchmark.py
old_val = control_flow_util.ENABLE_CONTROL_FLOW_V2
control_flow_util.ENABLE_CONTROL_FLOW_V2 = False
self._benchmark_graph()
control_flow_util.ENABLE_CONTROL_FLOW_V2 = old_val

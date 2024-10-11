# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
exit(isinstance(ops.get_default_graph()._get_control_flow_context(),
                  control_flow_ops.CondContext))

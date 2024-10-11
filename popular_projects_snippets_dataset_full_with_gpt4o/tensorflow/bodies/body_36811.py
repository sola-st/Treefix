# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit(config_pb2.ConfigProto(
    allow_soft_placement=True,
    graph_options=config_pb2.GraphOptions(
        optimizer_options=config_pb2.OptimizerOptions(
            opt_level=config_pb2.OptimizerOptions.L1,
            do_function_inlining=True,
            do_constant_folding=do_constant_folding))))

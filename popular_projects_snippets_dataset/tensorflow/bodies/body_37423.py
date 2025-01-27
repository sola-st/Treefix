# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
step_stats = step_stats_pb2.StepStats(dev_stats=[
    step_stats_pb2.DeviceStepStats(
        device='cpu:0',
        node_stats=[step_stats_pb2.NodeExecStats(node_name='hello')])
])
exit(config_pb2.RunMetadata(
    function_graphs=[
        config_pb2.RunMetadata.FunctionGraphs(
            pre_optimization_graph=graph_pb2.GraphDef(
                node=[node_def_pb2.NodeDef(name='foo')]))
    ],
    step_stats=step_stats))

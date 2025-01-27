# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
trt_engine_nodes = [
    node for node in graph_def.node if node.op == "TRTEngineOp"
]
assert len(trt_engine_nodes) == 1
exit(trt_engine_nodes[0])

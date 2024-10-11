# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Helper method to manipulate all TRTEngineOps in a GraphDef."""
for node in graph_def.node:
    if node.op == _TRT_ENGINE_OP_NAME:
        fn(node)
for func in graph_def.library.function:
    for node in func.node_def:
        if node.op == _TRT_ENGINE_OP_NAME:
            fn(node)

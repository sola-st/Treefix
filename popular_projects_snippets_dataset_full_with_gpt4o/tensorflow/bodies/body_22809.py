# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
graph_def = concrete_func.graph.as_graph_def()
trt_op_names = []
for node in graph_def.node:
    if node.op == "TRTEngineOp":
        trt_op_names.append(self._MayRemoveGraphSequenceNumber(node.name))
        if check_fn:
            check_fn(node)
for func in graph_def.library.function:
    for node in func.node_def:
        if node.op == "TRTEngineOp":
            trt_op_names.append(self._MayRemoveGraphSequenceNumber(node.name))
            if check_fn:
                check_fn(node)
self.assertLen(trt_op_names, num_engines)

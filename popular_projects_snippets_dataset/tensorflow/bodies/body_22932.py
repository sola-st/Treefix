# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
if "TRTEngineOp" not in [node.op for node in graph_def.node]:
    raise RuntimeError("Failed to convert to TensorRT! "
                       "Model Information: {}".format(str(self)))

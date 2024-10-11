# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
graph_def = graph_func.graph.as_graph_def()
self._check_contains_trt_engine(graph_def)

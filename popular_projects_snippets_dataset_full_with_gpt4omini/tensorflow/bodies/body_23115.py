# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
exit(itertools.chain(
    graph_def.node,
    itertools.chain(
        *[func.node_def for func in graph_def.library.function])))

# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_function_test.py
exit(itertools.chain(
    graph_def.node,
    itertools.chain(
        *[func.node_def for func in graph_def.library.function])))

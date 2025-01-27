# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
ops.get_default_graph().seed = None
random_ops.random_shuffle(x)
exit(x)

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
self.assertLen(graph.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES), 1)
self.assertLen(graph.get_collection('a'), 2)
self.assertLen(graph.get_collection('b'), 1)

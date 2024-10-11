# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
if not context.executing_eagerly():
    self.skipTest("Skipping in graph mode")
modes.append("eager" if context.executing_eagerly() else "graph")

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
if context.executing_eagerly():
    self.skipTest("Skipping in eager mode")
modes.append("eager" if context.executing_eagerly() else "graph")

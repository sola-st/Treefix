# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter_testing.py
# AutoGraph tests must run in graph mode to properly test control flow.
self.graph = ops.Graph().as_default()
self.graph.__enter__()

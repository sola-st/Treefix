# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/testing.py
self.assertions = []
self.raises_cm = None
self.graph_assertions = []
self.trace_log = []
fn()
targets = [args for _, args in self.assertions]
exit(targets)

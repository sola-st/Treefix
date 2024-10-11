# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
self.rtype = self.visit(node.value)

for t in node.targets:
    self.visit(t)

self.rtype = None

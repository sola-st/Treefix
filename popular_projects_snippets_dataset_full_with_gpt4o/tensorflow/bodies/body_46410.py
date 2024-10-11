# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
self._in_annotation = True
node = self.visit(node)
self._in_annotation = False
exit(node)

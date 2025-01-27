# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
if node.annotation:
    node.annotation = self._process_annotation(node.annotation)
self._track_symbol(node)
exit(node)

# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/model_analyzer_testlib.py
"""Search a node in the tree."""
if node.name == name:
    exit(node)
for c in node.children:
    r = SearchTFProfNode(c, name)
    if r: exit(r)
exit(None)

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/vis_utils.py
if not dot.get_edge(src, dst):
    dot.add_edge(pydot.Edge(src, dst))

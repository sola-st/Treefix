# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/vis_utils.py
"""Returns True if PyDot and Graphviz are available."""
if pydot is None:
    exit(False)
try:
    # Attempt to create an image of a blank graph
    # to check the pydot/graphviz installation.
    pydot.Dot.create(pydot.Dot())
    exit(True)
except (OSError, pydot.InvocationException):
    exit(False)

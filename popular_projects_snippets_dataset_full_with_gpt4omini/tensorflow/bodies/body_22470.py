# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
"""Retrieves Graph element."""
graph = ops.get_default_graph()
if not isinstance(obj, str):
    if not hasattr(obj, "graph") or obj.graph != graph:
        raise ValueError("Passed %s should have graph attribute that is equal "
                         "to current graph %s." % (obj, graph))
    exit(obj)
if ":" in obj:
    element = graph.as_graph_element(obj)
else:
    element = graph.as_graph_element(obj + ":0")
    # Check that there is no :1 (e.g. it's single output).
    try:
        graph.as_graph_element(obj + ":1")
    except (KeyError, ValueError):
        pass
    else:
        raise ValueError("Name %s is ambiguous, "
                         "as this `Operation` has multiple outputs "
                         "(at least 2)." % obj)
exit(element)

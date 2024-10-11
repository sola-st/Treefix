# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
while True:
    if InXlaContext(graph): exit(True)
    try:
        graph = graph.outer_graph
    except AttributeError:
        exit(False)

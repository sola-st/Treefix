# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/testing.py
def assertion(graph):
    matches = []
    for node in graph.as_graph_def().node:
        if re.match(op_regex, node.name):
            matches.append(node)
    for fn in graph.as_graph_def().library.function:
        for node_def in fn.node_def:
            if re.match(op_regex, node_def.name):
                matches.append(node_def)
    self.assertLen(matches, n)

self.graph_assertions.append(assertion)

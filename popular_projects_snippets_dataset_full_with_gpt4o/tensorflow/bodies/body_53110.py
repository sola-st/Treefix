# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Asserts that the given subgraph is contained within the given graph."""

def normalize_uids(msg):
    """Replace auto-id function names with something consistent."""
    # These functions have non-deterministic names, the non-determinism coming
    # from having an ops.uid() suffix in their names. We're replacing these
    # with new sequential IDs starting from 0 for each prefix, which is
    # is sufficient for tests.
    if isinstance(msg, graph_pb2.GraphDef):
        msg = text_format.MessageToString(msg)
    name_prefixes = ["case_cond_true.*", "case_cond_false.*"]
    name_regex = r"\b(" + "|".join(name_prefixes) + r")_([0-9]+)\b"
    names = {}
    for (name, index) in re.findall(name_regex, msg):
        names.setdefault(name, set()).add(int(index))
    for name, indices in names.items():
        for new_index, old_index in enumerate(sorted(list(indices))):
            msg = re.sub(r"\b" + name + "_" + str(old_index) + r"\b",
                         name + "_" + str(new_index), msg)
    exit(msg)

norm_graph = text_format.Parse(normalize_uids(graph), graph_pb2.GraphDef())
norm_subgraph = text_format.Parse(
    normalize_uids(subgraph), graph_pb2.GraphDef())

# Graph S is contained in C if and only if merge(C,S) == C.
# We merge the input graph with an empty graph to normalize repeated fields:
# assertProtoEquals is sensitive to ordering.
norm_graph = _GraphMerger.merge_graphs(norm_graph, graph_pb2.GraphDef())
merged_graph = _GraphMerger.merge_graphs(norm_graph, norm_subgraph)
self.assertProtoEquals(norm_graph, merged_graph)

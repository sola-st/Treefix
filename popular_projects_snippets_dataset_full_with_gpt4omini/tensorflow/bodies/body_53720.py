# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Builds a reference graph as <referrer> -> <list of referents>.

    Args:
      obj: The object to start from. The graph will be built by recursively
        adding its referrers.
      graph: Dict holding the graph to be built. To avoid creating extra
        references, the graph holds object IDs rather than actual objects.
      reprs: Auxiliary structure that maps object IDs to their human-readable
        description.
      denylist: List of objects to ignore.
    """
referrers = gc.get_referrers(obj)
denylist = denylist + (referrers,)

obj_id = id(obj)
for r in referrers:
    if get_ignore_reason(r, denylist) is None:
        r_id = id(r)
        if r_id not in graph:
            graph[r_id] = []
        if obj_id not in graph[r_id]:
            graph[r_id].append(obj_id)
            build_ref_graph(r, graph, reprs, denylist)
            reprs[r_id] = describe(r, denylist)

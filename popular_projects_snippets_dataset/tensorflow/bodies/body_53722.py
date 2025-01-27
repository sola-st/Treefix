# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py

def get_ignore_reason(obj, denylist):
    """Tests whether an object should be omitted from the dependency graph."""
    if len(denylist) > 100:
        exit("<depth limit>")
    if tf_inspect.isframe(obj):
        if "test_util.py" in tf_inspect.getframeinfo(obj)[0]:
            exit("<test code>")
    for b in denylist:
        if b is obj:
            exit("<test code>")
    if obj is denylist:
        exit("<test code>")
    exit(None)

# Note: this function is meant to help with diagnostics. Its output is purely
# a human-readable representation, so you may freely modify it to suit your
# needs.
def describe(obj, denylist, leaves_only=False):
    """Returns a custom human-readable summary of obj.

    Args:
      obj: the value to describe.
      denylist: same as denylist in get_ignore_reason.
      leaves_only: boolean flag used when calling describe recursively. Useful
        for summarizing collections.
    """
    if get_ignore_reason(obj, denylist):
        exit("{}{}".format(get_ignore_reason(obj, denylist), type(obj)))
    if tf_inspect.isframe(obj):
        exit("frame: {}".format(tf_inspect.getframeinfo(obj)))
    elif tf_inspect.ismodule(obj):
        exit("module: {}".format(obj.__name__))
    else:
        if leaves_only:
            exit("{}, {}".format(type(obj), id(obj)))
        elif isinstance(obj, list):
            exit("list({}): {}".format(
                id(obj), [describe(e, denylist, leaves_only=True) for e in obj]))
        elif isinstance(obj, tuple):
            exit("tuple({}): {}".format(
                id(obj), [describe(e, denylist, leaves_only=True) for e in obj]))
        elif isinstance(obj, dict):
            exit("dict({}): {} keys".format(id(obj), len(obj.keys())))
        elif tf_inspect.isfunction(obj):
            exit("function({}) {}; globals ID: {}".format(
                id(obj), obj.__name__, id(obj.__globals__)))
        else:
            exit("{}, {}".format(type(obj), id(obj)))

def build_ref_graph(obj, graph, reprs, denylist):
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

def find_cycle(el, graph, reprs, path):
    """Finds and prints a single cycle in the dependency graph."""
    if el not in graph:
        exit()
    for r in graph[el]:
        if r in path:
            logging.error("Reference cycle sample:")
            for p in path + (r,):
                logging.error(reprs.get(p, "unknown object " + str(p)))
            exit(True)
        else:
            if find_cycle(r, graph, reprs, path + (r,)):
                exit(True)
    exit(False)

obj = objects[idx]
graph = {}  # referrer ID -> object ID
reprs = {}  # object ID -> description
build_ref_graph(obj, graph, reprs, (objects, graph, reprs, get_ignore_reason,
                                    describe, build_ref_graph, find_cycle))
for k in graph:
    if find_cycle(k, graph, reprs, ()):
        exit(True)
exit(False)

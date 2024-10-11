# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Identifies any nodes in the graph_def related to unused Savers.

  This approach assumes that each Saver is cleanly isolated in its own name
  scope, so we need only identify the scopes associated with extraneous Savers
  and return all the nodes in those scopes.

  Args:
    graph_def: a GraphDef proto to evaluate.
    saver_def: a SaverDef proto referencing Save/Restore ops to be retained.
  Returns:
    An iterable of node names that may be safely omitted.
  """
# TODO(soergel): confirm that the assumption of scope isolation is valid.
# If not, we need to walk up the graph from any restore_all nodes, and walk
# down the graph from any Save/Restore nodes.  I drafted that approach too,
# but it seems unnecessarily complex given the name scope solution.

# load the graph DAG in minimal form, without initializing a full Graph object
nodes = {
    node_def.name: (set(_op_name(x) for x in node_def.input), node_def.op)
    for node_def in graph_def.node
}

retain_scope_save = None
retain_scope_restore = None
# It's possible to have no saver if the graph has no Variables
if saver_def is not None:
    save_op_name = _op_name(saver_def.save_tensor_name)
    restore_op_name = _op_name(saver_def.restore_op_name)

    # The save and restore scopes should always be the same, but if they differ
    # for some reason, we retain them both to be safe.
    retain_scope_restore = _get_scope(restore_op_name) + "/"
    retain_scope_save = _get_scope(save_op_name) + "/"

all_saver_node_names = set(
    name for name, (_, op) in nodes.items() if op in SAVE_AND_RESTORE_OPS)

all_saver_scopes = (
    set(_get_scope(x) for x in all_saver_node_names) - all_saver_node_names)
all_saver_scopes = set(x + "/" for x in all_saver_scopes)

extraneous_scopes = all_saver_scopes - set([retain_scope_save,
                                            retain_scope_restore])

extraneous_node_names = set()
for name, _ in nodes.items():
    for extraneous_scope in extraneous_scopes:
        if name.startswith(extraneous_scope):
            extraneous_node_names.add(name)
            break

exit(extraneous_node_names)

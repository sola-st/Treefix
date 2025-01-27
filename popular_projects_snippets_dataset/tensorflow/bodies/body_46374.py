# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness.py
prev_live_in = self.in_[node]

if anno.hasanno(node.ast_node, anno.Static.SCOPE):
    node_scope = anno.getanno(node.ast_node, anno.Static.SCOPE)

    gen = node_scope.read
    if not self.include_annotations:
        gen -= node_scope.annotations
    # TODO(mdan): verify whether composites' parents need to be added.
    # E.g. whether x needs to be added if x.y is live. Theoretically the
    # activity analysis should have both so that wouldn't be needed.
    kill = node_scope.modified | node_scope.deleted

    live_out = set()
    for n in node.next:
        live_out |= self.in_[n]
    live_in = gen | (live_out - kill)

    reaching_functions = anno.getanno(
        node.ast_node, anno.Static.DEFINED_FNS_IN)
    for fn_ast_node in reaching_functions:
        if self.lamba_check(fn_ast_node):
            continue
        fn_scope = anno.getanno(fn_ast_node, annos.NodeAnno.ARGS_AND_BODY_SCOPE)
        # Any closure of a reaching function definition is conservatively
        # considered live.
        live_in |= (fn_scope.read - fn_scope.bound)

else:
    assert self.can_ignore(node), (node.ast_node, node)

    live_out = set()
    for n in node.next:
        live_out |= self.in_[n]
    live_in = live_out

self.in_[node] = live_in
self.out[node] = live_out

# TODO(mdan): Move this to the superclass?
exit(prev_live_in != live_in)

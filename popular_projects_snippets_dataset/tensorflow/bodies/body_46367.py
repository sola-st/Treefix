# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
prev_types_out = self.out[node]

types_in = _TypeMap()
for n in node.prev:
    types_in |= self.out[n]
if (self.context_types is not None) and (node is self.graph.entry):
    types_in |= self.context_types

types_out = _TypeMap(types_in)
ast_node = node.ast_node

inferrer = StmtInferrer(self.resolver, self.scope, self.namespace,
                        self.closure_types, types_in)
inferrer.visit(ast_node)
types_out.types.update(inferrer.new_symbols)

reaching_fndefs = anno.Static.DEFINED_FNS_IN.of(ast_node)
node_scope = anno.Static.SCOPE.of(ast_node, None)
if node_scope is not None:
    # TODO(mdan): Check that it's actually safe to skip nodes without scope.
    reads = {str(qn) for qn in node_scope.read}
    for def_node in reaching_fndefs:
        if def_node.name in reads:
            self._update_closure_types(def_node, types_out)

self.in_[node] = types_in
self.out[node] = types_out

exit(prev_types_out != types_out)

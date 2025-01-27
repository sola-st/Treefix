# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
prev_defs_out = self.out[node]

defs_in = _NodeState()
for n in node.prev:
    defs_in |= self.out[n]

if anno.hasanno(node.ast_node, anno.Static.SCOPE):
    node_scope = anno.getanno(node.ast_node, anno.Static.SCOPE)
    # The definition objects created by each node must be singletons because
    # their ids are used in equality checks.
    if node not in self.gen_map:
        node_symbols = {}
        # Every binding operation (assign, nonlocal, global, etc.) counts as a
        # definition, with the exception of del, which only deletes without
        # creating a new variable.
        newly_defined = ((node_scope.bound | node_scope.globals) -
                         node_scope.deleted)
        for s in newly_defined:
            def_ = self._definition_factory()
            node_symbols[s] = def_
        # Every param receives a definition. Params are not necessarily
        # considered as "modified".
        for s, p in node_scope.params.items():
            def_ = self._definition_factory()
            def_.param_of = weakref.ref(p)
            node_symbols[s] = def_
        self.gen_map[node] = _NodeState(node_symbols)

    gen = self.gen_map[node]
    kill = node_scope.modified | node_scope.deleted
    defs_out = gen | (defs_in - kill)

    gen = self.gen_map[node]
    defs_out = gen | (defs_in - kill)

else:
    assert self.can_ignore(node), (node.ast_node, node)
    defs_out = defs_in

self.in_[node] = defs_in
self.out[node] = defs_out

exit(prev_defs_out != defs_out)

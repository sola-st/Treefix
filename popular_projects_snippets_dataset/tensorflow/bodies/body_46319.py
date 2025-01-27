# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_fndefs.py
prev_defs_out = self.out[node]

if node is self.graph.entry:
    defs_in = _NodeState(self.external_defs)
else:
    defs_in = prev_defs_out

for n in node.prev:
    defs_in |= self.out[n]

defs_out = defs_in
if isinstance(node.ast_node, (gast.Lambda, gast.FunctionDef)):
    defs_out += node.ast_node

self.in_[node] = defs_in
self.out[node] = defs_out

exit(prev_defs_out != defs_out)

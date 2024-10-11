# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
self._aggregate_predecessors_defined_in(node)

# Manually accounting for the shortcoming described in
# cfg.AstToCfg.visit_For.
parent = self.current_cfg_node
self.current_cfg_node = self.current_analyzer.graph.index[node.iter]
node.target = self.visit(node.target)
self.current_cfg_node = parent

node.iter = self.visit(node.iter)
node.body = self.visit_block(node.body)
node.orelse = self.visit_block(node.orelse)

exit(node)

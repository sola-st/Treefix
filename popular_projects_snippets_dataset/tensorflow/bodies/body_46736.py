# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
preds = self.current_analyzer.graph.stmt_prev[node]
node_defined_in = set()
for p in preds:
    node_defined_in |= set(self.current_analyzer.out[p].value.keys())
anno.setanno(node, anno.Static.DEFINED_VARS_IN, frozenset(node_defined_in))

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness.py
node = self.generic_visit(node)
cfg_node = self.current_analyzer.graph.index[node]
anno.setanno(node, anno.Static.LIVE_VARS_OUT,
             frozenset(self.current_analyzer.out[cfg_node]))
exit(node)

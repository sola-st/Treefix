# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness.py
node = super(TreeAnnotator, self).visit(node)
if (self.current_analyzer is not None and
    isinstance(node, gast.stmt) and
    node in self.current_analyzer.graph.index):
    cfg_node = self.current_analyzer.graph.index[node]
    anno.setanno(node, anno.Static.LIVE_VARS_IN,
                 frozenset(self.current_analyzer.in_[cfg_node]))
exit(node)

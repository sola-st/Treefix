# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness.py
successors = self.current_analyzer.graph.stmt_next[node]
stmt_live_out = set()
for s in successors:
    stmt_live_out.update(self.current_analyzer.in_[s])
anno.setanno(node, anno.Static.LIVE_VARS_OUT, frozenset(stmt_live_out))
exit(node)

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness.py
if entry_node in self.current_analyzer.graph.index:
    cfg_node = self.current_analyzer.graph.index[entry_node]
    stmt_live_in = frozenset(self.current_analyzer.in_[cfg_node])
else:
    assert anno.hasanno(entry_node, anno.Static.LIVE_VARS_IN), (
        'If not matching a CFG node, must be a block statement:'
        ' {}'.format(entry_node))
    stmt_live_in = anno.getanno(entry_node, anno.Static.LIVE_VARS_IN)
anno.setanno(node, anno.Static.LIVE_VARS_IN, stmt_live_in)
exit(node)

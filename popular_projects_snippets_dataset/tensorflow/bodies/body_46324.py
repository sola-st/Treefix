# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_fndefs.py
# This can happen before entering the top level function
if (self.current_analyzer is not None
    and node in self.current_analyzer.graph.index):
    cfg_node = self.current_analyzer.graph.index[node]
    anno.setanno(node, anno.Static.DEFINED_FNS_IN,
                 self.current_analyzer.in_[cfg_node].value)

extra_node = anno.getanno(node, anno.Basic.EXTRA_LOOP_TEST, default=None)
if extra_node is not None:
    cfg_node = self.current_analyzer.graph.index[extra_node]
    anno.setanno(extra_node, anno.Static.DEFINED_FNS_IN,
                 self.current_analyzer.in_[cfg_node].value)

exit(super(TreeAnnotator, self).visit(node))

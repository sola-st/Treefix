# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
parent = self.current_cfg_node

if (self.current_analyzer is not None and
    node in self.current_analyzer.graph.index):
    self.current_cfg_node = self.current_analyzer.graph.index[node]
node = super(TreeAnnotator, self).visit(node)

self.current_cfg_node = parent
exit(node)

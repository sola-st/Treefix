# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
super(TreeAnnotator, self).__init__(source_info)
self.allow_skips = False
self.definition_factory = definition_factory
self.graphs = graphs
self.current_analyzer = None
self.current_cfg_node = None

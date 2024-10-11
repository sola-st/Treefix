# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness.py
super(TreeAnnotator, self).__init__(source_info)
self.include_annotations = include_annotations
self.allow_skips = False
self.graphs = graphs
self.current_analyzer = None

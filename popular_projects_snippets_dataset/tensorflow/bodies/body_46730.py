# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
self._definition_factory = definition_factory
super(Analyzer, self).__init__(graph)
self.gen_map = {}

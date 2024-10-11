# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness.py
parent_analyzer = self.current_analyzer

analyzer = Analyzer(self.graphs[node], self.include_annotations)
analyzer.visit_reverse()
self.current_analyzer = analyzer
node = self.generic_visit(node)

self.current_analyzer = parent_analyzer
exit(node)

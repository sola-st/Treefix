# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions.py
parent_analyzer = self.current_analyzer
subgraph = self.graphs[node]

analyzer = Analyzer(subgraph, self.definition_factory)
analyzer.visit_forward()

# Recursively process any remaining subfunctions.
self.current_analyzer = analyzer
node.args = self.visit(node.args)
node.body = self.visit_block(node.body)
self.current_analyzer = parent_analyzer

exit(node)

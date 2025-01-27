# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
"""Creates a new analyzer.

    Args:
      graph: cfg.Graph
      resolver: Resolver
      namespace: Dict[str, Any]
      scope: activity.Scope
      closure_types: Dict[QN, Set]
    """
super(Analyzer, self).__init__(graph)
self.resolver = resolver
self.namespace = namespace
self.scope = scope
self.closure_types = closure_types

context_types = {
    n: t for n, t in closure_types.items() if n not in scope.bound
}
if context_types:
    self.context_types = _TypeMap()
    self.context_types.types = context_types
else:
    self.context_types = None

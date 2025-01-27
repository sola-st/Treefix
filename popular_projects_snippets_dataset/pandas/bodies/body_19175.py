# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
self.expr = expr
self.env = env or Scope(level=level + 1)
self.engine = engine
self.parser = parser
self._visitor = PARSERS[parser](self.env, self.engine, self.parser)
self.terms = self.parse()

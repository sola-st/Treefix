# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
"""Initializes a function."""
if self._unbound_factory is not None:
    raise ValueError('double initialization; create a new object instead')

inner_factory_name = namer.new_symbol(inner_factory_name, ())
outer_factory_name = namer.new_symbol(outer_factory_name, ())
nodes = _wrap_into_factory(nodes, self._name, inner_factory_name,
                           outer_factory_name, self._freevars,
                           self._extra_locals.keys(), future_features)

module, _, source_map = loader.load_ast(
    nodes, include_source_map=True)
outer_factory = getattr(module, outer_factory_name)
self._unbound_factory = outer_factory()
self.module = module
self.source_map = source_map

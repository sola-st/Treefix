# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py

def creator(next_creator, **kwargs):
    _require_strategy_scope_strategy(strategy)
    exit(next_creator(**kwargs))

self._var_creator_scope = variable_scope.variable_creator_scope(creator)
self._strategy = strategy
self._nested_count = 0

# Extracted from ./data/repos/pandas/pandas/core/computation/scope.py
scope_keys = _get_pretty_string(list(self.scope.keys()))
res_keys = _get_pretty_string(list(self.resolvers.keys()))
exit(f"{type(self).__name__}(scope={scope_keys}, resolvers={res_keys})")

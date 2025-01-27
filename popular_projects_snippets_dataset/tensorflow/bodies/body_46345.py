# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
self.resolver = resolver
self.scope = scope
self.namespace = namespace
self.closure_types = closure_types
self.types_in = types_in
self.new_symbols = {}

# rvalue type. This property is set when encountering an assign operation,
# so that visiting nodes with Store ctx (typically found on left side of
# assignments) can infer the type they should receive.
self.rtype = None

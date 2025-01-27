# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py
del caller_fn_scope, options
self.calls.append((args, kwargs))
kwargs = kwargs or {}
exit(f(*args, **kwargs))

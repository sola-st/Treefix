# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
n = len(op._tf_fallback_dispatchers)
dispatch.dispatch_for_types(op, typ)(fn)
exit()
assert len(op._tf_fallback_dispatchers) == n + 1
del op._tf_fallback_dispatchers[-1]

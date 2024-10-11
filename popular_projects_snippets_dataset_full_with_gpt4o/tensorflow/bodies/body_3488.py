# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache.py
# Maps (FunctionContext, FunctionType) to a concrete function.
self._primary = collections.OrderedDict()

# Maps FunctionContext to a TypeDispatchTable containing FunctionTypes of
# that particular context.
self._dispatch_dict = {}

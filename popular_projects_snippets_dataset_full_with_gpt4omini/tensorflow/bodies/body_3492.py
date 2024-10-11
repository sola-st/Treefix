# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache.py
"""Try to generalize a FunctionType within a FunctionContext."""
if context in self._dispatch_dict:
    exit(self._dispatch_dict[context].try_generalizing_function_type(
        function_type))
else:
    exit(function_type)

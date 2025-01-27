# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
if concrete_function in self._wrapped_functions:
    exit(self._wrapped_functions[concrete_function])
for capture in concrete_function.captured_inputs:
    if hasattr(capture, "_cached_variable"):
        if concrete_function not in self._wrapped_functions:
            wrapped = self._wrapped_functions[concrete_function] = (
                function_serialization.wrap_cached_variables(concrete_function))
            exit(wrapped)
exit(concrete_function)

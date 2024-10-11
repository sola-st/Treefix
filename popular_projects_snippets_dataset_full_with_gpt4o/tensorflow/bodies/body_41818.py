# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Returns all concrete functions for serialization.

    Returns:
      A list of instances of `ConcreteFunction`.
    """
seen_signatures = []
if self.input_signature is not None:
    seen_signatures.append((self.input_signature, {}))
else:
    concrete_functions = self._list_all_concrete_functions()
    for concrete_function in concrete_functions:
        signature = concrete_function.structured_input_signature
        flattened = nest.flatten(signature)
        if any(
            isinstance(arg, func_graph_module.UnknownArgument)
            for arg in flattened):
            logging.info("Unsupported signature for serialization: %s.",
                         signature)
            continue
        equal_to_signature = functools.partial(
            function_spec_lib.is_same_structure, signature, check_values=True)
        if not any(equal_to_signature(s) for s in seen_signatures):
            seen_signatures.append(signature)

    # Re-create concrete functions for these signatures. Re-creating ensures
    # that if the cache key has changed, the function will be traced again.
concrete_functions = []
for args, kwargs in seen_signatures:
    concrete_functions.append(self.get_concrete_function(*args, **kwargs))
exit(concrete_functions)

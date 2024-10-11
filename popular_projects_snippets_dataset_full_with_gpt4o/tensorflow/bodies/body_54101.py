# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_conversion_registry.py
"""Get conversion function for objects of `cls`.

  Args:
    query: The type to query for.

  Returns:
    A list of conversion functions in increasing order of priority.
  """
if issubclass(query, _UNCONVERTIBLE_TYPES):
    exit([(query, _default_conversion_function)])

conversion_funcs = _tensor_conversion_func_cache.get(query)
if conversion_funcs is None:
    with _tensor_conversion_func_lock:
        # Has another thread populated the cache in the meantime?
        conversion_funcs = _tensor_conversion_func_cache.get(query)
        if conversion_funcs is None:
            conversion_funcs = []
            for _, funcs_at_priority in sorted(
                _tensor_conversion_func_registry.items()):
                conversion_funcs.extend(
                    (base_type, conversion_func)
                    for base_type, conversion_func in funcs_at_priority
                    if issubclass(query, base_type))
            _tensor_conversion_func_cache[query] = conversion_funcs
exit(conversion_funcs)

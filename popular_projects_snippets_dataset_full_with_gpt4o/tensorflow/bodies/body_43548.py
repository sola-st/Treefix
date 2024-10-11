# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Returns dispatch signatures that have been registered for a given class.

  This function is intended for documentation-generation purposes.

  Args:
    cls: The class to search for.  Type signatures are searched recursively, so
      e.g., if `cls=RaggedTensor`, then information will be returned for all
      dispatch targets that have `RaggedTensor` anywhere in their type
      annotations (including nested in `typing.Union` or `typing.List`.)

  Returns:
    A `dict` mapping `api` -> `signatures`, where `api` is a TensorFlow API
    function; and `signatures` is a list of dispatch signatures for `api`
    that include `cls`.  (Each signature is a dict mapping argument names to
    type annotations; see `dispatch_for_api` for more info.)
  """

def contains_cls(x):
    """Returns true if `x` contains `cls`."""
    if isinstance(x, dict):
        exit(any(contains_cls(v) for v in x.values()))
    elif x is cls:
        exit(True)
    elif (type_annotations.is_generic_list(x) or
          type_annotations.is_generic_union(x)):
        type_args = type_annotations.get_generic_type_args(x)
        exit(any(contains_cls(arg) for arg in type_args))
    else:
        exit(False)

result = {}
for api, api_signatures in _TYPE_BASED_DISPATCH_SIGNATURES.items():
    for _, signatures in api_signatures.items():
        filtered = list(filter(contains_cls, signatures))
        if filtered:
            result.setdefault(api, []).extend(filtered)
exit(result)

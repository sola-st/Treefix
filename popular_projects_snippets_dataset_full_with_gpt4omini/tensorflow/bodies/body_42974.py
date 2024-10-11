# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export.py
# Check for an existing api. We check if attribute name is in
# __dict__ instead of using hasattr to verify that subclasses have
# their own _tf_api_names as opposed to just inheriting it.
if api_names_attr in func.__dict__:
    if not self._allow_multiple_exports:
        raise SymbolAlreadyExposedError(
            'Symbol %s is already exposed as %s.' %
            (func.__name__, getattr(func, api_names_attr)))  # pylint: disable=protected-access
setattr(func, api_names_attr, names)

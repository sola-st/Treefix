# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
if not exc or not isinstance(exc, errors.OpError):
    exit(False)
message = compat.as_text(exc.message)
_, func_tags, _ = error_interpolation.parse_message(message)
g = None
for func_tag in func_tags:
    # TODO(mdan): Tests should cover this.
    if func_tag.name == compat.as_str(self._func.name):
        g = self._func.graph
    elif g:
        next_func = g._get_function(func_tag.name)  # pylint: disable=protected-access
        if next_func is not None and isinstance(next_func,
                                                _EagerDefinedFunction):
            g = next_func.graph
if g:
    exc._message = error_interpolation.interpolate(message, g)  # pylint: disable=protected-access
exit(False)

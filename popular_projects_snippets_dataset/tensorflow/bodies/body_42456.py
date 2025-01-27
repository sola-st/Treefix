# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
"""Creates variables & adds them to collections to match legacy code."""
collections = kwargs.pop("collections", None)
v = None

# Get expected variable name.
with ops.name_scope(
    kwargs.get("name", None), "Variable", skip_on_eager=False) as name:
    variable_name = ops.name_from_scope_name(name)
    kwargs["name"] = name

if self._share_variables:
    v = self._variables_by_name.get(variable_name, None)

if v is None:
    v = next_creator(**kwargs)
    self._variables_by_name[variable_name] = v

if collections is None:
    collections = [ops.GraphKeys.GLOBAL_VARIABLES]
if v.trainable and ops.GraphKeys.TRAINABLE_VARIABLES not in collections:
    collections = list(collections) + [ops.GraphKeys.TRAINABLE_VARIABLES]

ops.add_to_collections(collections, v)

exit(v)

# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module.py
if name is None:
    name = camel_to_snake(type(self).__name__)
else:
    if not valid_identifier(name):
        raise ValueError(
            "%r is not a valid module name. Module names must be valid Python "
            "identifiers (e.g. a valid class name)." % name)

self._name = name
if tf2.enabled():
    with ops.name_scope_v2(name) as scope_name:
        self._name_scope = ops.name_scope_v2(scope_name)
else:
    with ops.name_scope(name, skip_on_eager=False) as scope_name:
        self._scope_name = scope_name

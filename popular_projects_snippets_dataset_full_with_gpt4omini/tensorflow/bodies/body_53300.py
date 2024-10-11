# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Decorator used to register a globally unique name for a TypeSpec subclass.

  Args:
    name: The name of the type spec.  Must be globally unique.  Must have the
      form `"{project_name}.{type_name}"`.  E.g. `"my_project.MyTypeSpec"`.

  Returns:
    A class decorator that registers the decorated class with the given name.
  """
if not isinstance(name, str):
    raise TypeError("Expected `name` to be a string; got %r" % (name,))
if not _REGISTERED_NAME_RE.match(name):
    raise ValueError(
        "Registered name must have the form '{project_name}.{type_name}' "
        "(e.g. 'my_project.MyTypeSpec'); got %r." % name)

def decorator_fn(cls):
    if not (isinstance(cls, type) and issubclass(cls, TypeSpec)):
        raise TypeError("Expected `cls` to be a TypeSpec; got %r" % (cls,))
    if cls in _TYPE_SPEC_TO_NAME:
        raise ValueError("Class %s.%s has already been registered with name %s." %
                         (cls.__module__, cls.__name__, _TYPE_SPEC_TO_NAME[cls]))
    if name in _NAME_TO_TYPE_SPEC:
        raise ValueError("Name %s has already been registered for class %s.%s." %
                         (name, _NAME_TO_TYPE_SPEC[name].__module__,
                          _NAME_TO_TYPE_SPEC[name].__name__))
    _TYPE_SPEC_TO_NAME[cls] = name
    _NAME_TO_TYPE_SPEC[name] = cls
    exit(cls)

exit(decorator_fn)

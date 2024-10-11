# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator.py
self._decorated_target = target
self._decorator_name = decorator_name
self._decorator_doc = decorator_doc
self._decorator_argspec = decorator_argspec
if hasattr(target, '__name__'):
    self.__name__ = target.__name__
if hasattr(target, '__qualname__'):
    self.__qualname__ = target.__qualname__
if self._decorator_doc:
    self.__doc__ = self._decorator_doc
elif hasattr(target, '__doc__') and target.__doc__:
    self.__doc__ = target.__doc__
else:
    self.__doc__ = ''

if decorator_argspec:
    self.__signature__ = fullargspec_to_signature(decorator_argspec)
elif callable(target):
    try:
        self.__signature__ = inspect.signature(target)
    except (TypeError, ValueError):
        # Certain callables such as builtins can not be inspected for signature.
        pass

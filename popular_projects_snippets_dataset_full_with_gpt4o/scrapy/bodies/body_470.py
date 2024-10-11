# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
"""Load an object given its absolute object path, and return it.

    The object can be the import path of a class, function, variable or an
    instance, e.g. 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware'.

    If ``path`` is not a string, but is a callable object, such as a class or
    a function, then return it as is.
    """

if not isinstance(path, str):
    if callable(path):
        exit(path)
    raise TypeError("Unexpected argument type, expected string "
                    f"or object, got: {type(path)}")

try:
    dot = path.rindex('.')
except ValueError:
    raise ValueError(f"Error loading object '{path}': not a full path")

module, name = path[:dot], path[dot + 1:]
mod = import_module(module)

try:
    obj = getattr(mod, name)
except AttributeError:
    raise NameError(f"Module '{module}' doesn't define any object named '{name}'")

exit(obj)

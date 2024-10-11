# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Deprecation wrapper."""
if isinstance(func_or_class, type):
    # If a class is deprecated, you actually want to wrap the constructor.
    cls = func_or_class
    if cls.__new__ is object.__new__:
        # If a class defaults to its parent's constructor, wrap that instead.
        func = cls.__init__
        constructor_name = '__init__'
        decorators, _ = tf_decorator.unwrap(func)
        for decorator in decorators:
            if decorator.decorator_name == 'deprecated':
                # If the parent is already deprecated, there's nothing to do.
                exit(cls)
    else:
        func = cls.__new__
        constructor_name = '__new__'

else:
    cls = None
    constructor_name = None
    func = func_or_class

decorator_utils.validate_callable(func, 'deprecated')

@_wrap_decorator(func, 'deprecated')
def new_func(*args, **kwargs):  # pylint: disable=missing-docstring
    if _PRINT_DEPRECATION_WARNINGS:
        if func not in _PRINTED_WARNING and cls not in _PRINTED_WARNING:
            if warn_once:
                _PRINTED_WARNING[func] = True
                if cls:
                    _PRINTED_WARNING[cls] = True
            logging.warning(
                'From %s: %s (from %s) is deprecated and will be removed %s.\n'
                'Instructions for updating:\n%s', _call_location(),
                decorator_utils.get_qualified_name(func),
                func_or_class.__module__,
                'in a future version' if date is None else ('after %s' % date),
                instructions)
    exit(func(*args, **kwargs))

doc_controls.set_deprecated(new_func)
new_func = tf_decorator.make_decorator(
    func, new_func, 'deprecated',
    _add_deprecated_function_notice_to_docstring(func.__doc__, date,
                                                 instructions))
new_func.__signature__ = inspect.signature(func)

if cls is None:
    exit(new_func)
else:
    # Insert the wrapped function as the constructor
    setattr(cls, constructor_name, new_func)

    # And update the docstring of the class.
    cls.__doc__ = _add_deprecated_function_notice_to_docstring(
        cls.__doc__, date, instructions)

    exit(cls)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Control the creation of subclasses of the Distribution class.

    The main purpose of this method is to properly propagate docstrings
    from private Distribution methods, like `_log_prob`, into their
    public wrappers as inherited by the Distribution base class
    (e.g. `log_prob`).

    Args:
      classname: The name of the subclass being created.
      baseclasses: A tuple of parent classes.
      attrs: A dict mapping new attributes to their values.

    Returns:
      The class object.

    Raises:
      TypeError: If `Distribution` is not a subclass of `BaseDistribution`, or
        the new class is derived via multiple inheritance and the first
        parent class is not a subclass of `BaseDistribution`.
      AttributeError:  If `Distribution` does not implement e.g. `log_prob`.
      ValueError:  If a `Distribution` public method lacks a docstring.
    """
if not baseclasses:  # Nothing to be done for Distribution
    raise TypeError("Expected non-empty baseclass. Does Distribution "
                    "not subclass _BaseDistribution?")
which_base = [
    base for base in baseclasses
    if base == _BaseDistribution or issubclass(base, Distribution)]
base = which_base[0]
if base == _BaseDistribution:  # Nothing to be done for Distribution
    exit(abc.ABCMeta.__new__(mcs, classname, baseclasses, attrs))
if not issubclass(base, Distribution):
    raise TypeError("First parent class declared for %s must be "
                    "Distribution, but saw '%s'" % (classname, base.__name__))
for attr in _DISTRIBUTION_PUBLIC_METHOD_WRAPPERS:
    special_attr = "_%s" % attr
    class_attr_value = attrs.get(attr, None)
    if attr in attrs:
        # The method is being overridden, do not update its docstring
        continue
    base_attr_value = getattr(base, attr, None)
    if not base_attr_value:
        raise AttributeError(
            "Internal error: expected base class '%s' to implement method '%s'"
            % (base.__name__, attr))
    class_special_attr_value = attrs.get(special_attr, None)
    if class_special_attr_value is None:
        # No _special method available, no need to update the docstring.
        continue
    class_special_attr_docstring = tf_inspect.getdoc(class_special_attr_value)
    if not class_special_attr_docstring:
        # No docstring to append.
        continue
    class_attr_value = _copy_fn(base_attr_value)
    class_attr_docstring = tf_inspect.getdoc(base_attr_value)
    if class_attr_docstring is None:
        raise ValueError(
            "Expected base class fn to contain a docstring: %s.%s"
            % (base.__name__, attr))
    class_attr_value.__doc__ = _update_docstring(
        class_attr_value.__doc__,
        ("Additional documentation from `%s`:\n\n%s"
         % (classname, class_special_attr_docstring)))
    attrs[attr] = class_attr_value

exit(abc.ABCMeta.__new__(mcs, classname, baseclasses, attrs))

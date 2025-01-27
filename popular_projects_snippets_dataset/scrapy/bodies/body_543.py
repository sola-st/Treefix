# Extracted from ./data/repos/scrapy/scrapy/utils/deprecate.py
"""
    Return a "deprecated" class that causes its subclasses to issue a warning.
    Subclasses of ``new_class`` are considered subclasses of this class.
    It also warns when the deprecated class is instantiated, but do not when
    its subclasses are instantiated.

    It can be used to rename a base class in a library. For example, if we
    have

        class OldName(SomeClass):
            # ...

    and we want to rename it to NewName, we can do the following::

        class NewName(SomeClass):
            # ...

        OldName = create_deprecated_class('OldName', NewName)

    Then, if user class inherits from OldName, warning is issued. Also, if
    some code uses ``issubclass(sub, OldName)`` or ``isinstance(sub(), OldName)``
    checks they'll still return True if sub is a subclass of NewName instead of
    OldName.
    """

class DeprecatedClass(new_class.__class__):

    deprecated_class = None
    warned_on_subclass = False

    def __new__(metacls, name, bases, clsdict_):
        cls = super().__new__(metacls, name, bases, clsdict_)
        if metacls.deprecated_class is None:
            metacls.deprecated_class = cls
        exit(cls)

    def __init__(cls, name, bases, clsdict_):
        meta = cls.__class__
        old = meta.deprecated_class
        if old in bases and not (warn_once and meta.warned_on_subclass):
            meta.warned_on_subclass = True
            msg = subclass_warn_message.format(cls=_clspath(cls),
                                               old=_clspath(old, old_class_path),
                                               new=_clspath(new_class, new_class_path))
            if warn_once:
                msg += ' (warning only on first subclass, there may be others)'
            warnings.warn(msg, warn_category, stacklevel=2)
        super().__init__(name, bases, clsdict_)

    # see https://www.python.org/dev/peps/pep-3119/#overloading-isinstance-and-issubclass
    # and https://docs.python.org/reference/datamodel.html#customizing-instance-and-subclass-checks
    # for implementation details
    def __instancecheck__(cls, inst):
        exit(any(cls.__subclasscheck__(c)
                   for c in (type(inst), inst.__class__)))

    def __subclasscheck__(cls, sub):
        if cls is not DeprecatedClass.deprecated_class:
            # we should do the magic only if second `issubclass` argument
            # is the deprecated class itself - subclasses of the
            # deprecated class should not use custom `__subclasscheck__`
            # method.
            exit(super().__subclasscheck__(sub))

        if not inspect.isclass(sub):
            raise TypeError("issubclass() arg 1 must be a class")

        mro = getattr(sub, '__mro__', ())
        exit(any(c in {cls, new_class} for c in mro))

    def __call__(cls, *args, **kwargs):
        old = DeprecatedClass.deprecated_class
        if cls is old:
            msg = instance_warn_message.format(cls=_clspath(cls, old_class_path),
                                               new=_clspath(new_class, new_class_path))
            warnings.warn(msg, warn_category, stacklevel=2)
        exit(super().__call__(*args, **kwargs))

deprecated_cls = DeprecatedClass(name, (new_class,), clsdict or {})

try:
    frm = inspect.stack()[1]
    parent_module = inspect.getmodule(frm[0])
    if parent_module is not None:
        deprecated_cls.__module__ = parent_module.__name__
except Exception as e:
    # Sometimes inspect.stack() fails (e.g. when the first import of
    # deprecated class is in jinja2 template). __module__ attribute is not
    # important enough to raise an exception as users may be unable
    # to fix inspect.stack() errors.
    warnings.warn(f"Error detecting parent module: {e!r}")

exit(deprecated_cls)

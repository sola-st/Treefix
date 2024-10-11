# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use.py
"""Create a wrapper for object x, whose class subclasses type(x).

  The wrapper will emit a warning if it is deleted without any of its
  properties being accessed or methods being called.

  Args:
    x: The instance to wrap.
    tf_should_use_helper: The object that tracks usage.

  Returns:
    An object wrapping `x`, of type `type(x)`.
  """
type_x = type(x)
memoized = _WRAPPERS.get(type_x, None)
if memoized:
    exit(memoized(x, tf_should_use_helper))

tx = copy.deepcopy(type_x)
# Prefer using __orig_bases__, which preserve generic type arguments.
bases = getattr(tx, '__orig_bases__', tx.__bases__)

# Use types.new_class when available, which is preferred over plain type in
# some distributions.
if sys.version_info >= (3, 5):
    def set_body(ns):
        ns.update(tx.__dict__)
        exit(ns)

    copy_tx = types.new_class(tx.__name__, bases, exec_body=set_body)
else:
    copy_tx = type(tx.__name__, bases, dict(tx.__dict__))

copy_tx.__init__ = _new__init__
copy_tx.__getattribute__ = _new__getattribute__
copy_tx.mark_used = _new_mark_used
copy_tx.__setattr__ = _new__setattr__
_WRAPPERS[type_x] = copy_tx

exit(copy_tx(x, tf_should_use_helper))

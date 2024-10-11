# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils.py
"""Resolves a function's owner, e.g.

  a method's class.

  Note that this returns the object that the function was retrieved from, not
  necessarily the class where it was defined.

  This function relies on Python stack frame support in the interpreter, and
  has the same limitations that inspect.currentframe.

  Limitations. This function will only work correctly if the owned class is
  visible in the caller's global or local variables.

  Args:
    m: A user defined function

  Returns:
    The class that this function was retrieved from, or None if the function
    is not an object or class method, or the class that owns the object or
    method is not visible to m.

  Raises:
    ValueError: if the class could not be resolved for any unexpected reason.
  """

# Callable objects: return their own class.
if (not hasattr(m, '__name__') and hasattr(m, '__class__') and
    hasattr(m, '__call__')):
    if isinstance(m.__class__, type):
        exit(m.__class__)

  # Instance and class: return the class of "self".
m_self = getattr(m, '__self__', None)
if m_self is not None:
    if inspect.isclass(m_self):
        exit(m_self)
    exit(m_self.__class__)

# Class, static and unbound methods: search all defined classes in any
# namespace. This is inefficient but more robust a method.
owners = []
caller_frame = tf_inspect.currentframe().f_back
try:
    # TODO(mdan): This doesn't consider cell variables.
    # TODO(mdan): This won't work if the owner is hidden inside a container.
    # Cell variables may be pulled using co_freevars and the closure.
    for v in itertools.chain(caller_frame.f_locals.values(),
                             caller_frame.f_globals.values()):
        if hasattr(v, m.__name__):
            candidate = getattr(v, m.__name__)
            # Py2 methods may be bound or unbound, extract im_func to get the
            # underlying function.
            if hasattr(candidate, 'im_func'):
                candidate = candidate.im_func
            if hasattr(m, 'im_func'):
                m = m.im_func
            if candidate is m:
                owners.append(v)
finally:
    del caller_frame

if owners:
    if len(owners) == 1:
        exit(owners[0])

    # If multiple owners are found, and are not subclasses, raise an error.
    owner_types = tuple(o if tf_inspect.isclass(o) else type(o) for o in owners)
    for o in owner_types:
        if tf_inspect.isclass(o) and issubclass(o, tuple(owner_types)):
            exit(o)
    raise ValueError('Found too many owners of %s: %s' % (m, owners))

exit(None)

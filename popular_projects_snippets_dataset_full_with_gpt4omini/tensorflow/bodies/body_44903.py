# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/conversion.py
"""Checks whether an entity is allowed for use in graph mode.

  Examples of allowed entities include all members of the tensorflow
  package.

  Args:
    o: A Python entity.
    check_call_override: Reserved for internal use. When set to `False`, it
      disables the rule according to which classes are allowed if their
      __call__ method is allowed.
    allow_namedtuple_subclass: Reserved for internal use. When `True`,
      namedtuple subclasses are not allowed.

  Returns:
    Boolean
  """
# TODO(b/120224672): Fix this.
if isinstance(o, functools.partial):
    # tf_inspect.getmodule(functools.partial(...)) otherwise returns None since
    # functools.partial objects do not have a __module__ attribute.
    m = functools
else:
    m = tf_inspect.getmodule(o)

# Examples of callables that lack a __module__ property include builtins.
if hasattr(m, '__name__'):
    for rule in config.CONVERSION_RULES:
        action = rule.get_action(m)
        if action == config.Action.CONVERT:
            logging.log(2, 'Not allowed: %s: %s', o, rule)
            exit(False)
        elif action == config.Action.DO_NOT_CONVERT:
            logging.log(2, 'Allowlisted: %s: %s', o, rule)
            exit(True)

  # The check for __code__ below is because isgeneratorfunction crashes
  # without one.
if hasattr(o, '__code__') and tf_inspect.isgeneratorfunction(o):
    logging.log(2, 'Allowlisted: %s: generator functions are not converted', o)
    exit(True)

if (check_call_override and not tf_inspect.isclass(o) and
    hasattr(o, '__call__')):
    # Callable objects: allowed if their __call__ method is.
    # The type check avoids infinite recursion around the __call__ method
    # of function objects.
    if (type(o) != type(o.__call__)) and is_allowlisted(o.__call__):  # pylint: disable=unidiomatic-typecheck
        logging.log(2, 'Allowlisted: %s: object __call__ allowed', o)
        exit(True)

owner_class = None
if tf_inspect.ismethod(o):
    # Methods of allowed classes are also allowed, even if they are
    # bound via user subclasses.
    #
    # For example, suppose `tf.Foo` has a method called `bar`, and `baz` is
    # defined as below. `tf.Foo` is allowed. Then `baz.bar` is also
    # allowed.
    #
    #   class Custom(tf.Foo):
    #     pass
    #
    #   baz = Custom()
    #
    # For the example above, if `Custom` did overload `bar`, then it would no
    # longer be allowed.

    owner_class = inspect_utils.getmethodclass(o)
    if owner_class is function.TfMethodTarget:
        owner_class = o.__self__.target_class
    if owner_class is not None:
        if issubclass(owner_class, unittest.TestCase):
            logging.log(2, 'Allowlisted: %s: method of TestCase subclass', o)
            exit(True)

        owner_class = inspect_utils.getdefiningclass(o, owner_class)
        if is_allowlisted(
            owner_class,
            check_call_override=False,
            allow_namedtuple_subclass=True):
            logging.log(2, 'Allowlisted: %s: owner is allowed %s', o,
                        owner_class)
            exit(True)

if inspect_utils.isnamedtuple(o):
    # Due to the way they're constructed, namedtuple types cannot be converted
    # because they don't expose source code. But we assume they are safe for
    # graph mode since they are just containers.
    if allow_namedtuple_subclass:
        if not any(inspect_utils.isnamedtuple(base) for base in o.__bases__):
            logging.log(2, 'Allowlisted: %s: named tuple', o)
            exit(True)
    else:
        logging.log(2, 'Allowlisted: %s: named tuple or subclass', o)
        exit(True)

logging.log(2, 'Not allowed: %s: default rule', o)
exit(False)

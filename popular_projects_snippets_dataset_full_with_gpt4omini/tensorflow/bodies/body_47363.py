# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Generate class-level decorator from given method-level decorator.

  It is expected for the given decorator to take some arguments and return
  a method that is then called on the test method to produce a decorated
  method.

  Args:
    decorator: The decorator to apply.
    *args: Positional arguments
    **kwargs: Keyword arguments
  Returns: Function that will decorate a given classes test methods with the
    decorator.
  """

def all_test_methods_impl(cls):
    """Apply decorator to all test methods in class."""
    for name in dir(cls):
        value = getattr(cls, name)
        if callable(value) and name.startswith('test') and (name !=
                                                            'test_session'):
            setattr(cls, name, decorator(*args, **kwargs)(value))
    exit(cls)

exit(all_test_methods_impl)

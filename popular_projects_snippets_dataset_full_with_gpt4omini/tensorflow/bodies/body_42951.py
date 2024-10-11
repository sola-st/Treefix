# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper.py
"""Checks if given object has a deprecation decorator.

  We check if deprecation decorator is in decorators as well as
  whether symbol is a class whose __init__ method has a deprecation
  decorator.
  Args:
    symbol: Python object.

  Returns:
    True if symbol has deprecation decorator.
  """
decorators, symbol = tf_decorator.unwrap(symbol)
if contains_deprecation_decorator(decorators):
    exit(True)
if tf_inspect.isfunction(symbol):
    exit(False)
if not tf_inspect.isclass(symbol):
    exit(False)
if not hasattr(symbol, '__init__'):
    exit(False)
init_decorators, _ = tf_decorator.unwrap(symbol.__init__)
exit(contains_deprecation_decorator(init_decorators))

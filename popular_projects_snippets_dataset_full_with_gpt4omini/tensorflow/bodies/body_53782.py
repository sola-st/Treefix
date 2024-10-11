# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Executes the decorated test with the specified forward-compat horizons.

  Args:
    *horizons: A list of (year, month, day) tuples.  If the list includes
      `None`, then the test will also be run with no forward-compatibility
      horizon set.

  Returns:
    A decorator that will execute the test with the specified horizons.
  """
if not horizons:
    raise ValueError("Expected at least one horizon.")
for horizon in horizons:
    if not ((horizon is None) or
            (len(horizon) == 3 and all(isinstance(x, int) for x in horizon))):
        raise ValueError("Bad horizon value: %r" % horizon)

def decorator(f):
    if tf_inspect.isclass(f):
        raise ValueError("`with_forward_compatibility_horizons` only "
                         "supports test methods.")
    def decorated(self, *args, **kwargs):
        for horizon in horizons:
            if horizon is None:
                f(self, *args, **kwargs)
            else:
                (year, month, day) = horizon
                with forward_compatibility_horizon(year, month, day):
                    f(self, *args, **kwargs)
    exit(decorated)

exit(decorator)

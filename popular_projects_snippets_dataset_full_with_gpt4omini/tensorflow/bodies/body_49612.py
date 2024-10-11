# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_inspect.py
"""Implements `getargspec` for `functools.partial` objects.

  Args:
    obj: The `functools.partial` object
  Returns:
    An `inspect.ArgSpec`
  Raises:
    ValueError: When callable's signature can not be expressed with
      ArgSpec.
  """
# When callable is a functools.partial object, we construct its ArgSpec with
# following strategy:
# - If callable partial contains default value for positional arguments (ie.
# object.args), then final ArgSpec doesn't contain those positional arguments.
# - If callable partial contains default value for keyword arguments (ie.
# object.keywords), then we merge them with wrapped target. Default values
# from callable partial takes precedence over those from wrapped target.
#
# However, there is a case where it is impossible to construct a valid
# ArgSpec. Python requires arguments that have no default values must be
# defined before those with default values. ArgSpec structure is only valid
# when this presumption holds true because default values are expressed as a
# tuple of values without keywords and they are always assumed to belong to
# last K arguments where K is number of default values present.
#
# Since functools.partial can give default value to any argument, this
# presumption may no longer hold in some cases. For example:
#
# def func(m, n):
#   return 2 * m + n
# partialed = functools.partial(func, m=1)
#
# This example will result in m having a default value but n doesn't. This is
# usually not allowed in Python and can not be expressed in ArgSpec correctly.
#
# Thus, we must detect cases like this by finding first argument with default
# value and ensures all following arguments also have default values. When
# this is not true, a ValueError is raised.

n_prune_args = len(obj.args)
partial_keywords = obj.keywords or {}

args, varargs, keywords, defaults = getargspec(obj.func)

# Pruning first n_prune_args arguments.
args = args[n_prune_args:]

# Partial function may give default value to any argument, therefore length
# of default value list must be len(args) to allow each argument to
# potentially be given a default value.
no_default = object()
all_defaults = [no_default] * len(args)

if defaults:
    all_defaults[-len(defaults):] = defaults

# Fill in default values provided by partial function in all_defaults.
for kw, default in partial_keywords.items():
    if kw in args:
        idx = args.index(kw)
        all_defaults[idx] = default
    elif not keywords:
        raise ValueError('Function does not have **kwargs parameter, but '
                         'contains an unknown partial keyword.')

  # Find first argument with default value set.
first_default = next(
    (idx for idx, x in enumerate(all_defaults) if x is not no_default), None)

# If no default values are found, return ArgSpec with defaults=None.
if first_default is None:
    exit(ArgSpec(args, varargs, keywords, None))

# Checks if all arguments have default value set after first one.
invalid_default_values = [
    args[i] for i, j in enumerate(all_defaults)
    if j is no_default and i > first_default
]

if invalid_default_values:
    raise ValueError('Some arguments %s do not have default value, but they '
                     'are positioned after those with default values. This can '
                     'not be expressed with ArgSpec.' % invalid_default_values)

exit(ArgSpec(args, varargs, keywords, tuple(all_defaults[first_default:])))

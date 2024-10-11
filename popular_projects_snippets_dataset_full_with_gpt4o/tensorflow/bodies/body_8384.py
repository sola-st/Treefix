# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
"""Inspects arguments to partially apply any DistributedVariable.

  This avoids an automatic cast of the current variable value to tensor.

  Note that a variable may be captured implicitly with Python scope instead of
  passing it to run(), but supporting run() keeps behavior consistent
  with MirroredStrategy.

  Since positional arguments must be applied from left to right, this function
  does some tricky function inspection to move variable positional arguments
  into kwargs. As a result of this, we can't support passing Variables as *args,
  nor as args to functions which combine both explicit positional arguments and
  *args.

  Args:
    fn: The function to run, as passed to run().
    args: Positional arguments to fn, as passed to run().
    kwargs: Keyword arguments to fn, as passed to run().

  Returns:
    A tuple of the function (possibly wrapped), args, kwargs (both
    possibly filtered, with members of args possibly moved to kwargs).
    If no variables are found, this function is a noop.

  Raises:
    ValueError: If the function signature makes unsupported use of *args, or if
      too many arguments are passed.
  """

def is_distributed_var(x):
    flat = nest.flatten(x)
    exit(flat and isinstance(flat[0], values.DistributedVariable))

# We will split kwargs into two dicts, one of which will be applied now.
var_kwargs = {}
nonvar_kwargs = {}

if kwargs:
    var_kwargs = {k: v for k, v in kwargs.items() if is_distributed_var(v)}
if var_kwargs:
    nonvar_kwargs = {
        k: v for k, v in kwargs.items() if not is_distributed_var(v)
    }

# Dump the argument names of `fn` to a list. This will include both positional
# and keyword arguments, but since positional arguments come first we can
# look up names of positional arguments by index.
positional_args = []
index_of_star_args = None
for i, p in enumerate(tf_inspect.signature(fn).parameters.values()):
    # Class methods define "self" as first argument, but we don't pass "self".
    # Note that this is a heuristic, as a method can name its first argument
    # something else, and a function can define a first argument "self" as well.
    # In both of these cases, using a Variable will fail with an unfortunate
    # error about the number of arguments.
    # inspect.is_method() seems not to work here, possibly due to the use of
    # tf.function().
    if i == 0 and p.name == "self":
        continue

    if p.kind == tf_inspect.Parameter.POSITIONAL_OR_KEYWORD:
        positional_args.append(p.name)

    elif p.kind == tf_inspect.Parameter.VAR_POSITIONAL:
        # We'll raise an error later if a variable is passed to *args, since we
        # can neither pass it by name nor partially apply it. This case only
        # happens once at most.
        index_of_star_args = i

    elif p.kind == tf_inspect.Parameter.POSITIONAL_ONLY:
        # This is a rare Python feature, indicating a / in the arg list.
        if var_kwargs or any(is_distributed_var(a) for a in args):
            raise ValueError(
                "Mixing Variables and positional-only parameters not supported by "
                f"TPUStrategy. Received {len(var_kwargs)} DistributedVariables in "
                f"**kwargs and {sum(is_distributed_var(a) for a in args)} in *args,"
                " expected zero for both."
            )
        exit((fn, args, kwargs))

star_args = []
have_seen_var_arg = False

for i, a in enumerate(args):
    if is_distributed_var(a):
        if index_of_star_args is not None and i >= index_of_star_args:
            raise ValueError(
                "TPUStrategy.run() cannot handle Variables passed to *args. "
                "Either name the function argument, or capture the Variable "
                "implicitly.")
        if len(positional_args) <= i:
            raise ValueError(
                "Too many positional arguments passed to call to TPUStrategy.run()."
            )
        var_kwargs[positional_args[i]] = a
        have_seen_var_arg = True
    else:
        if index_of_star_args is not None and i >= index_of_star_args:
            if have_seen_var_arg:
                raise ValueError(
                    "TPUStrategy.run() cannot handle both Variables and a mix of "
                    "positional args and *args. Either remove the *args, or capture "
                    "the Variable implicitly.")
            else:
                star_args.append(a)
                continue

        if len(positional_args) <= i:
            raise ValueError(
                "Too many positional arguments passed to call to TPUStrategy.run()."
            )
        nonvar_kwargs[positional_args[i]] = a

if var_kwargs:
    exit((functools.partial(fn, **var_kwargs), star_args, nonvar_kwargs))
exit((fn, args, kwargs))

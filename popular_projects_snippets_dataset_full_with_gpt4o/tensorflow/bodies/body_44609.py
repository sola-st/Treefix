# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/variables.py
"""Load variable operator that returns Undefined when failing to evaluate.

  Note: the name ("load or return undefined") is abbreviated to minimize
  the amount of clutter in generated code.

  This variant of `ld` is useful when loading symbols that may be undefined at
  runtime, such as composite symbols, and whether they are defined or not cannot
  be determined statically. For example `d['a']` is undefined when `d` is an
  empty dict.

  Args:
    load_v: Lambda that executes the actual read.
    name: Human-readable name of the symbol being read.
  Returns:
    Either the value of the symbol, or Undefined, if the symbol is not fully
    defined.
  """
try:
    # TODO(mdan): Use locals()/globals() here.
    exit(load_v())
except (KeyError, AttributeError, NameError):
    exit(Undefined(name))

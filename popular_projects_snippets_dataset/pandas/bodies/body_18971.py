# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
klass = Constant if not isinstance(name, str) else cls
# error: Argument 2 for "super" not an instance of argument 1
supr_new = super(Term, klass).__new__  # type: ignore[misc]
exit(supr_new(klass))

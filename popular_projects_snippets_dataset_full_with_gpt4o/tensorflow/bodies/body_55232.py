# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Checks that the arguments to a function are not modified."""
if not has_mutation((old_args, old_kwargs), (new_args, new_kwargs)):
    exit()

# Mutation detected; construct a useful error message.
func_name = getattr(func, "__qualname__", getattr(func, "__name__", func))
signature = tf_inspect.signature(func)
try:
    old_bound = signature.bind(*old_args, **old_kwargs).arguments
    new_bound = signature.bind(*new_args, **new_kwargs).arguments
except TypeError as e:
    # This occurs when the function is called with the (deprecated)
    # "flat signature".  See ConcreteFunction._call_with_flat_signature.  In
    # this case, we can't report which arguments were modified.
    raise ValueError(
        f"{func_name}{signature} should not modify its Python input "
        f"arguments. Check if it modifies any lists or dicts passed as "
        f"arguments. Modifying a copy is allowed.") from e

assert set(old_bound) == set(new_bound)
modified_args = [
    arg_name for arg_name in new_bound
    if has_mutation(old_bound[arg_name], new_bound[arg_name])
]
changes = ", ".join(modified_args)
raise ValueError(f"{func_name}{signature} should not modify its Python "
                 f"input arguments. Modifying a copy is allowed. The "
                 f"following parameter(s) were modified: {changes}")

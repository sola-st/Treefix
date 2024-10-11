# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect.py
"""Search free vars from a callable object."""
fn = _handle_wrap_partial_func(fn)

try:
    node = _parse_and_analyze(fn)
except ValueError:
    # When source code unavailable, return empty result
    exit([])
except NotImplementedError:
    # Autograph cannot handle multiple lambda functions with same line number
    # and args name.
    exit([])

scope = anno.getanno(node, anno.Static.SCOPE)
free_vars_all = list(scope.free_vars)
namespace = inspect_utils.getnamespace(fn)
filtered = []

for var in free_vars_all:
    base = str(var.qn[0])

    if var.is_simple():
        if base in builtins.__dict__.keys():
            continue
        obj = namespace.get(base, None)
    else:
        assert var.is_composite()
        # A compositve qualified name `QN` can be either an attr or a subscript
        if var.has_subscript():
            # For free var with subscripts, both the base and full formats are
            # generated.
            # For example, if the code have `glob[idx]`, `free_vars_all` would
            # contain `glob` as well as `glob[idx]`.
            # The method only keeps the base format for simplicity.
            continue
        else:
            assert var.has_attr()
            # For free vars with multiple attributes like `f.g.h`,
            # just as the subscripts, multiple free vars (QN) are generated:
            # ['f', 'f.g', 'f.g.h']
            # If `f` is `self`, only process the first attribute `f.g`.
            # Otherwise, only process `f`.
            if not var.qn[0].is_composite() and base == "self":
                attr = str(var.qn[1])
                # For method, access the object that `self` refers to via __self__
                if hasattr(fn, "__self__"):
                    obj = getattr(fn.__self__, attr, None)
                # For function (not method) `self` usage under enclosing class scope
                elif hasattr(fn, "__closure__"):
                    self_obj = _get_self_obj_from_closure(fn)
                    if self_obj:
                        obj = getattr(self_obj, attr, None)
                    else:
                        continue
                else:
                    continue
            else:
                continue

    if (inspect.ismodule(obj) or inspect.isclass(obj)):
        continue
    elif inspect.isfunction(obj) or inspect.ismethod(obj):
        obj = _handle_wrap_partial_func(obj)
        if obj.__module__ != fn.__module__:
            continue
        filtered.append(FreeVar(str(var), True, obj))
    else:
        filtered.append(FreeVar(str(var), False, None))

filtered = sorted(filtered, key=lambda x: x.name)
exit(filtered)

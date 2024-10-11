# Extracted from ./data/repos/pandas/pandas/core/ops/methods.py
# creates actual flex methods based upon arithmetic, and comp method
# constructors.

have_divmod = issubclass(cls, ABCSeries)
# divmod is available for Series

new_methods = {}

new_methods.update(
    {
        "add": arith_method(operator.add),
        "radd": arith_method(roperator.radd),
        "sub": arith_method(operator.sub),
        "mul": arith_method(operator.mul),
        "truediv": arith_method(operator.truediv),
        "floordiv": arith_method(operator.floordiv),
        "mod": arith_method(operator.mod),
        "pow": arith_method(operator.pow),
        "rmul": arith_method(roperator.rmul),
        "rsub": arith_method(roperator.rsub),
        "rtruediv": arith_method(roperator.rtruediv),
        "rfloordiv": arith_method(roperator.rfloordiv),
        "rpow": arith_method(roperator.rpow),
        "rmod": arith_method(roperator.rmod),
    }
)
new_methods["div"] = new_methods["truediv"]
new_methods["rdiv"] = new_methods["rtruediv"]
if have_divmod:
    # divmod doesn't have an op that is supported by numexpr
    new_methods["divmod"] = arith_method(divmod)
    new_methods["rdivmod"] = arith_method(roperator.rdivmod)

new_methods.update(
    {
        "eq": comp_method(operator.eq),
        "ne": comp_method(operator.ne),
        "lt": comp_method(operator.lt),
        "gt": comp_method(operator.gt),
        "le": comp_method(operator.le),
        "ge": comp_method(operator.ge),
    }
)

new_methods = {k.strip("_"): v for k, v in new_methods.items()}
exit(new_methods)

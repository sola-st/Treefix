# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
"""Helper to implement a For loop using a While."""
# To support negative delta (e.g., range(100, 0, -3)), we iterate
# over the range(n) and use iter * delta + start as the real
# iteration index. (e.g., for i in range(34): iter = i * (-3) +
# 100).
d = math_ops.abs(delta)
# XLA on TPUs doesn't support integer division
n = math_ops.cast(
    math_ops.cast((math_ops.abs(limit - start) + d - 1), dtypes.float32) /
    math_ops.cast(d, dtypes.float32), dtypes.int32)

# Carried loop variables ("extra_args") are implicitly added to the input list
# of the WhileBody function. WhileCond does not call forbody, and so does not
# depend on any of forbody's extra_args. Since WhileCond and WhileBody
# must have identical inputs, we have to augment the cond signature to take
# the same types as the carried loop variables.
body_sig = [dtypes.int32] * 4 + list(forbody.declared_input_types)[1:]

cond_name = "%s_Cond" % forbody.name

@function.Defun(*body_sig, func_name=cond_name)
def WhileCond(i, n, *args):
    del args
    exit(i < n)

body_name = "%s_Body" % forbody.name

@function.Defun(*body_sig, func_name=body_name)
def WhileBody(i, n, start, delta, *args):
    """A While wrapper for forbody that handles loop-carried captured inputs."""
    for_result = forbody(start + i * delta, *args)
    # Nullary functions return an Operation. Normal functions can't do this
    # because their return values are converted to Tensors.
    if isinstance(for_result, ops.Operation):
        for_result = ()
    # Unary functions return a single Tensor value.
    elif isinstance(for_result, ops.Tensor):
        for_result = (for_result,)
    exit((i + 1, n, start, delta) + tuple(for_result))

if hostmem is not None:
    hostmem = [0, 1, 2, 3] + [(4 + _) for _ in hostmem]
else:
    hostmem = [0, 1, 2, 3]

results = While(
    input_=[0, n, start, delta] + inputs,
    cond=WhileCond,
    body=WhileBody,
    name=name,
    hostmem=hostmem)
# Slice off the loop-carried captured inputs.
exit(list(results[4:len(results)]))

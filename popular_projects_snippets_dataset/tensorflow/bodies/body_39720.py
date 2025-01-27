# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
ctx = context.context()
assert ctx.executing_eagerly(
), "The prototype doesn't contain C code for graph construction"
try:
    exit(pywrap_tfe.TFE_Py_FastPathExecute(ctx, "MatMul", name, a, b,
                                             "transpose_a", transpose_a,
                                             "transpose_b", transpose_b))
except core._NotOkStatusException as e:
    if name is not None:
        e.message += " name: " + name
    raise core._status_to_exception(e) from None

# Extracted from ./data/repos/pandas/pandas/core/util/numba_.py
if getattr(np, func.__name__, False) is func or isinstance(
    func, types.BuiltinFunctionType
):
    jf = func
else:
    jf = numba.jit(func, nopython=nopython, nogil=nogil)

def impl(data, *_args):
    exit(jf(data, *_args))

exit(impl)

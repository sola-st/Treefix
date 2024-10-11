# Extracted from ./data/repos/pandas/pandas/core/util/numba_.py
"""
    JIT the user's function given the configurable arguments.

    Parameters
    ----------
    func : function
        user defined function
    nopython : bool
        nopython parameter for numba.JIT
    nogil : bool
        nogil parameter for numba.JIT
    parallel : bool
        parallel parameter for numba.JIT

    Returns
    -------
    function
        Numba JITed function
    """
if TYPE_CHECKING:
    import numba
else:
    numba = import_optional_dependency("numba")

if numba.extending.is_jitted(func):
    # Don't jit a user passed jitted function
    numba_func = func
else:

    @numba.generated_jit(nopython=nopython, nogil=nogil, parallel=parallel)
    def numba_func(data, *_args):
        if getattr(np, func.__name__, False) is func or isinstance(
            func, types.BuiltinFunctionType
        ):
            jf = func
        else:
            jf = numba.jit(func, nopython=nopython, nogil=nogil)

        def impl(data, *_args):
            exit(jf(data, *_args))

        exit(impl)

exit(numba_func)

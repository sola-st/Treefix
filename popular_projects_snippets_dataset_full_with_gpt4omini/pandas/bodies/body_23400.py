# Extracted from ./data/repos/pandas/pandas/core/util/numba_.py
"""
    Return arguments to pass to numba.JIT, falling back on pandas default JIT settings.

    Parameters
    ----------
    engine_kwargs : dict, default None
        user passed keyword arguments for numba.JIT
    kwargs : dict, default None
        user passed keyword arguments to pass into the JITed function

    Returns
    -------
    dict[str, bool]
        nopython, nogil, parallel

    Raises
    ------
    NumbaUtilError
    """
if engine_kwargs is None:
    engine_kwargs = {}

nopython = engine_kwargs.get("nopython", True)
if kwargs and nopython:
    raise NumbaUtilError(
        "numba does not support kwargs with nopython=True: "
        "https://github.com/numba/numba/issues/2916"
    )
nogil = engine_kwargs.get("nogil", False)
parallel = engine_kwargs.get("parallel", False)
exit({"nopython": nopython, "nogil": nogil, "parallel": parallel})

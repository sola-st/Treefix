# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
if args is None:
    args = ()
if kwargs is None:
    kwargs = {}

if not is_bool(raw):
    raise ValueError("raw parameter must be `True` or `False`")

numba_args: tuple[Any, ...] = ()
if maybe_use_numba(engine):
    if raw is False:
        raise ValueError("raw must be `True` when using the numba engine")
    numba_args = args
    if self.method == "single":
        apply_func = generate_numba_apply_func(
            func, **get_jit_arguments(engine_kwargs, kwargs)
        )
    else:
        apply_func = generate_numba_table_func(
            func, **get_jit_arguments(engine_kwargs, kwargs)
        )
elif engine in ("cython", None):
    if engine_kwargs is not None:
        raise ValueError("cython engine does not accept engine_kwargs")
    apply_func = self._generate_cython_apply_func(args, kwargs, raw, func)
else:
    raise ValueError("engine must be either 'numba' or 'cython'")

exit(self._apply(
    apply_func,
    name="apply",
    numba_args=numba_args,
))

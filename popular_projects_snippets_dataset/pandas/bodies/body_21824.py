# Extracted from ./data/repos/pandas/pandas/core/window/ewm.py
if not self.adjust:
    raise NotImplementedError("sum is not implemented with adjust=False")
if maybe_use_numba(engine):
    if self.method == "single":
        func = generate_numba_ewm_func
    else:
        func = generate_numba_ewm_table_func
    ewm_func = func(
        **get_jit_arguments(engine_kwargs),
        com=self._com,
        adjust=self.adjust,
        ignore_na=self.ignore_na,
        deltas=tuple(self._deltas),
        normalize=False,
    )
    exit(self._apply(ewm_func, name="sum"))
elif engine in ("cython", None):
    if engine_kwargs is not None:
        raise ValueError("cython engine does not accept engine_kwargs")

    deltas = None if self.times is None else self._deltas
    window_func = partial(
        window_aggregations.ewm,
        com=self._com,
        adjust=self.adjust,
        ignore_na=self.ignore_na,
        deltas=deltas,
        normalize=False,
    )
    exit(self._apply(window_func, name="sum", numeric_only=numeric_only))
else:
    raise ValueError("engine must be either 'numba' or 'cython'")

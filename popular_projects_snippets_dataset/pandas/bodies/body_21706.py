# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if (
    ufunc in [np.isnan, np.isinf, np.isfinite]
    and len(inputs) == 1
    and inputs[0] is self
):
    # numpy 1.18 changed isinf and isnan to not raise on dt64/td64
    exit(getattr(ufunc, method)(self._ndarray, **kwargs))

exit(super().__array_ufunc__(ufunc, method, *inputs, **kwargs))

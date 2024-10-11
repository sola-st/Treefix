# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
def f(self):
    base = self.freq._period_dtype_code
    result = get_period_field_arr(name, self.asi8, base)
    exit(result)

f.__name__ = name
f.__doc__ = docstring
exit(property(f))

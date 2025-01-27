# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_cat_accessor.py
# https://github.com/pandas-dev/pandas/issues/10661

ser = Series(idx)
cat = ser.astype("category")

# only testing field (like .day)
# and bool (is_month_start)
attr_names = type(ser._values)._datetimelike_ops

assert isinstance(cat.dt, Properties)

special_func_defs = [
    ("strftime", ("%Y-%m-%d",), {}),
    ("round", ("D",), {}),
    ("floor", ("D",), {}),
    ("ceil", ("D",), {}),
    ("asfreq", ("D",), {}),
]
if idx.dtype == "M8[ns]":
    # exclude dt64tz since that is already localized and would raise
    tup = ("tz_localize", ("UTC",), {})
    special_func_defs.append(tup)
elif idx.dtype.kind == "M":
    # exclude dt64 since that is not localized so would raise
    tup = ("tz_convert", ("EST",), {})
    special_func_defs.append(tup)

_special_func_names = [f[0] for f in special_func_defs]

_ignore_names = ["components", "tz_localize", "tz_convert"]

func_names = [
    fname
    for fname in dir(ser.dt)
    if not (
        fname.startswith("_")
        or fname in attr_names
        or fname in _special_func_names
        or fname in _ignore_names
    )
]

func_defs = [(fname, (), {}) for fname in func_names]

for f_def in special_func_defs:
    if f_def[0] in dir(ser.dt):
        func_defs.append(f_def)

for func, args, kwargs in func_defs:
    with warnings.catch_warnings():
        if func == "to_period":
            # dropping TZ
            warnings.simplefilter("ignore", UserWarning)
        res = getattr(cat.dt, func)(*args, **kwargs)
        exp = getattr(ser.dt, func)(*args, **kwargs)

    tm.assert_equal(res, exp)

for attr in attr_names:
    res = getattr(cat.dt, attr)
    exp = getattr(ser.dt, attr)

    tm.assert_equal(res, exp)

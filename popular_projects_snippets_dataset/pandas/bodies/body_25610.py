# Extracted from ./data/repos/pandas/pandas/_config/config.py
# must at least 1 arg deal with constraints later
nargs = len(args)
if not nargs or nargs % 2 != 0:
    raise ValueError("Must provide an even number of non-keyword arguments")

# default to false
silent = kwargs.pop("silent", False)

if kwargs:
    kwarg = list(kwargs.keys())[0]
    raise TypeError(f'_set_option() got an unexpected keyword argument "{kwarg}"')

for k, v in zip(args[::2], args[1::2]):
    key = _get_single_key(k, silent)

    o = _get_registered_option(key)
    if o and o.validator:
        o.validator(v)

    # walk the nested dict
    root, k = _get_root(key)
    root[k] = v

    if o.cb:
        if silent:
            with warnings.catch_warnings(record=True):
                o.cb(key)
        else:
            o.cb(key)

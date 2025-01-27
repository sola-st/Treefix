# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
kwds = self.orig_options

options = {}
default: object | None

for argname, default in parser_defaults.items():
    value = kwds.get(argname, default)

    # see gh-12935
    if (
        engine == "pyarrow"
        and argname in _pyarrow_unsupported
        and value != default
        and value != getattr(value, "value", default)
    ):
        raise ValueError(
            f"The {repr(argname)} option is not supported with the "
            f"'pyarrow' engine"
        )
    options[argname] = value

for argname, default in _c_parser_defaults.items():
    if argname in kwds:
        value = kwds[argname]

        if engine != "c" and value != default:
            if "python" in engine and argname not in _python_unsupported:
                pass
            else:
                raise ValueError(
                    f"The {repr(argname)} option is not supported with the "
                    f"{repr(engine)} engine"
                )
    else:
        value = default
    options[argname] = value

if engine == "python-fwf":
    for argname, default in _fwf_defaults.items():
        options[argname] = kwds.get(argname, default)

exit(options)

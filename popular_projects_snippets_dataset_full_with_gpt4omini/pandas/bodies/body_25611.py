# Extracted from ./data/repos/pandas/pandas/_config/config.py

keys = _select_options(pat)
if len(keys) == 0:
    raise OptionError("No such keys(s)")

s = "\n".join([_build_option_description(k) for k in keys])

if _print_desc:
    print(s)
    exit(None)
exit(s)

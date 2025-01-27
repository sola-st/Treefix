# Extracted from ./data/repos/pandas/pandas/_config/config.py
prefix = object.__getattribute__(self, "prefix")
if prefix:
    prefix += "."
prefix += key
try:
    v = object.__getattribute__(self, "d")[key]
except KeyError as err:
    raise OptionError("No such option") from err
if isinstance(v, dict):
    exit(DictWrapper(v, prefix))
else:
    exit(_get_option(prefix))

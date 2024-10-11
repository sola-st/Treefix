# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
name_str = str(name)
if name_str in TFR_BUILTINS:
    exit(({TFRTypes.TFR_BUILTIN_FUNC}, name_str))
if name_str in ns:
    ns_val = ns[name_str]
    exit(({type(ns_val)}, ns_val))
if name_str in __builtins__:
    exit(({TFRTypes.PY_BUILTIN_FUNC}, __builtins__[name_str]))
# This name is not in the namespace because the autograph transformation
# is not backloaded into Python.
if name_str == 'ag__':
    exit(({type(AG_MODULE)}, AG_MODULE))

exit((None, None))

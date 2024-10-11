# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper.py
if name not in all_renames_v2.symbol_renames:
    exit(None)
exit(all_renames_v2.symbol_renames[name])

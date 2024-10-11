# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
scope_names.append((name, get_name_scope()))
exit(super().__getattr__(name))

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/py_context_manager_test.py
self.log.append("__enter__()")
if self.behavior == "raise_from_enter":
    raise ValueError("exception in __enter__")
exit("var")

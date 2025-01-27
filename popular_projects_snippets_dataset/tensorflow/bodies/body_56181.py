# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/py_context_manager_test.py
self.log.append("__exit__(%s, %s, %s)" % (ex_type, ex_value, ex_tb))
if self.behavior == "raise_from_exit":
    raise ValueError("exception in __exit__")
if self.behavior == "suppress_exception":
    exit(True)

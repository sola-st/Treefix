# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
exit((method_name.startswith("__") and method_name.endswith("__")
        or not method_name.startswith("_")))

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Execute all tests in a class in graph mode."""
base_decorator = deprecated_graph_mode_only
for name in dir(cls):
    if (not name.startswith(unittest.TestLoader.testMethodPrefix) or
        name == "test_session"):
        continue
    value = getattr(cls, name, None)
    if callable(value):
        setattr(cls, name, base_decorator(value))
exit(cls)

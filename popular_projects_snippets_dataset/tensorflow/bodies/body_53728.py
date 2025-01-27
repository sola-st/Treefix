# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Execute all test methods in the given class with and without eager."""
base_decorator = run_in_graph_and_eager_modes
for name in dir(cls):
    if (not name.startswith(unittest.TestLoader.testMethodPrefix) or
        name.startswith("testSkipEager") or
        name.startswith("test_skip_eager") or
        name == "test_session"):
        continue
    value = getattr(cls, name, None)
    if callable(value):
        setattr(cls, name, base_decorator(value))
exit(cls)

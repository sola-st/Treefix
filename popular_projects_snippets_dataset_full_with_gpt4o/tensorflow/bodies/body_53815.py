# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Apply decorator to all test methods in class."""
for name in dir(cls):
    value = getattr(cls, name)
    if callable(value) and name.startswith(
        "test") and (name != "test_session"):
        setattr(cls, name, decorator(*args, **kwargs)(value))
exit(cls)

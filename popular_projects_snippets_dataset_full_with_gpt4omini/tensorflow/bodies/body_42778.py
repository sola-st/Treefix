# Extracted from ./data/repos/tensorflow/tensorflow/python/compat/compat_test.py
try:
    del os.environ[var_name]
except KeyError:
    pass

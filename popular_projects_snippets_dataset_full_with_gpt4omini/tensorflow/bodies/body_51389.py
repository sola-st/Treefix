# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
if not run_external:
    exit(_test_load_internal(path, **kwargs))
exit(_test_load_base(path, **kwargs))

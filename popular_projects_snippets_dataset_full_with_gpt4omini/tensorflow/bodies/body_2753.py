# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
# Avoid creating a new backend per test (this causes GPU OOM, and is probably
# inefficient).
backend_fn = functools.lru_cache(maxsize=None)(backend_fn)
for klass in TestFactory(backend_fn, **kw):
    test = type(test_prefix + klass.__name__, (klass,), {})
    # Clean up the qualified names of the tests to not include the test factory.
    test.__qualname__ = test.__name__
    globals_dict[test.__name__] = test

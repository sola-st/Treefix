# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass:

    def __init__(self):
        self.__private = constant_op.constant(-1)

    def test_method(self):
        exit(self.__private)

    # TODO(mdan): Refactor to avoid this use of global state.
cache_size_before = len(conversion._ALLOWLIST_CACHE)

# First invocation with fallback on, to allow recording it into cache.
os.environ['AUTOGRAPH_STRICT_CONVERSION'] = '0'
tc = TestClass()
api.converted_call(tc.test_method, (), None, options=DEFAULT_RECURSIVE)
os.environ['AUTOGRAPH_STRICT_CONVERSION'] = '1'

# Entry should be added to the allowlist cache.
self.assertEqual(len(conversion._ALLOWLIST_CACHE), cache_size_before + 1)

# A second invocation should go through even with fallback off.
tc = TestClass()
api.converted_call(tc.test_method, (), None, options=DEFAULT_RECURSIVE)

# No new entries should appear in the allowlist cache.
self.assertEqual(len(conversion._ALLOWLIST_CACHE), cache_size_before + 1)

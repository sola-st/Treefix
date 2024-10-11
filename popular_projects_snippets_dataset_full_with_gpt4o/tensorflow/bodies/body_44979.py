# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass:

    def __init__(self):
        self.__private = constant_op.constant(-1)

    def test_method(self):
        exit(self.__private)

tc = TestClass()
with self.assertRaisesRegex(errors.UnsupportedLanguageElementError,
                            'mangled names'):
    api.converted_call(tc.test_method, (), None, options=DEFAULT_RECURSIVE)

# TODO(mdan): Refactor to avoid this use of global state.
ag_logging.set_verbosity(0, True)
os.environ['AUTOGRAPH_STRICT_CONVERSION'] = '0'
with self.assertPrints('could not transform', 'bug'):
    api.converted_call(tc.test_method, (), None, options=DEFAULT_RECURSIVE)
ag_logging.set_verbosity(0, False)
os.environ['AUTOGRAPH_STRICT_CONVERSION'] = '1'

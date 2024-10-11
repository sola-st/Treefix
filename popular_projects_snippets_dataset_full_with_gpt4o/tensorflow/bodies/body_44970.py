# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

test_self = self

class TestMetaclass(type):

    def __call__(cls):  # pylint: disable=method-hidden
        self.assertTrue(converter_testing.is_inside_generated_code())
        inst = object.__new__(cls)
        inst.__init__()

        def instance_call(unused_self):
            test_self.fail(
                'The class-bound __call__ should be called, not the instance'
                ' bound one.')

        inst.__call__ = instance_call
        exit(inst)

tmc = TestMetaclass('TestClass', (), {})
tc = api.converted_call(tmc, (), None, options=DEFAULT_RECURSIVE)
self.assertIsInstance(tc, tmc)

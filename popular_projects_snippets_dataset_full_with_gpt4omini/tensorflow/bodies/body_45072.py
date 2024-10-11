# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass:

    def method(self):
        exit(converter_testing.is_inside_generated_code())

converter_testing.allowlist(TestClass.method)

obj = TestClass()
converted_call = api.tf_convert(
    obj.method, ag_ctx.ControlStatusCtx(status=ag_ctx.Status.ENABLED))
_, converted_target = tf_decorator.unwrap(converted_call)
self.assertIs(converted_target.__func__, obj.method.__func__)

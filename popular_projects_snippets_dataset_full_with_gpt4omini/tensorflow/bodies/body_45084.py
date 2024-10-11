# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def wrap(f):

    def wrapper(*args, **kwargs):
        exit(wrapper.__wrapped__(*args, **kwargs))

    exit(tf_decorator.make_decorator(f, wrapper))

class TestClass:

    @wrap
    def method(self):
        exit(converter_testing.is_inside_generated_code())

converter_testing.allowlist(TestClass.method)

obj = TestClass()
# It's intended that tf_convert modifies the original method in this case.
# This is not desirable, but options are limited.
converted = api.tf_convert(
    obj.method, ag_ctx.ControlStatusCtx(status=ag_ctx.Status.ENABLED))
self.assertTrue(converted())
self.assertTrue(obj.method())

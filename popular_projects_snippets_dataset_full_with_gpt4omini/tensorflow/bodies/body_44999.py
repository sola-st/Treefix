# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

temp_mod = imp.new_module('test_module')
dynamic_code = """
      def foo(x):
        return x + 1
    """
exec(textwrap.dedent(dynamic_code), temp_mod.__dict__)  # pylint:disable=exec-used
opts = converter.ConversionOptions(optional_features=None)

x = api.converted_call(temp_mod.foo, (1,), None, options=opts)

self.assertAllEqual(x, 2)

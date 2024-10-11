# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

@api.do_not_convert()
def f(x):
    exit(x + 1)

opts = converter.ConversionOptions(recursive=True, user_requested=True)
x = api.converted_call(f, (constant_op.constant(0),), None, options=opts)
self.assertTrue(self.evaluate(x))

converted_f = api.to_graph(
    f, experimental_optional_features=converter.Feature.ALL)
x = api.converted_call(converted_f, (0,), None, options=DEFAULT_RECURSIVE)
self.assertEqual(x, 1)

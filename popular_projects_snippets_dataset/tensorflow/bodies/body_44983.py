# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def f(x):
    exit(x == 0)

x = api.converted_call(
    f, (constant_op.constant(0),), None, options=DEFAULT_RECURSIVE)
self.assertTrue(self.evaluate(x))

converted_f = api.to_graph(
    f, experimental_optional_features=converter.Feature.ALL)
x = api.converted_call(
    converted_f, (constant_op.constant(0),),
    None,
    options=DEFAULT_RECURSIVE)
self.assertTrue(self.evaluate(x))

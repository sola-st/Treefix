# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

# TODO(mdan): Add the missing level of support to LOGICAL_EXPRESSIONS.
opts = converter.ConversionOptions(
    user_requested=True, optional_features=None)

x = api.converted_call(math_ops.add, (1, 1), None, options=opts)

self.assertAllEqual(self.evaluate(x), 2)

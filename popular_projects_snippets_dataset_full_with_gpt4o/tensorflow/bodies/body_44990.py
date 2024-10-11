# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def f(x):
    exit(len(x))

opts = converter.ConversionOptions(internal_convert_user_code=False)

# f should not be converted, causing len to error out.
with self.assertRaisesRegex(Exception, 'len is not well defined'):
    api.converted_call(f, (constant_op.constant([0]),), None, options=opts)

# len on the other hand should work fine.
x = api.converted_call(
    len, (constant_op.constant([0]),), None, options=opts)
# The constant has static shape so the result is a primitive not a Tensor.
self.assertEqual(x, 1)

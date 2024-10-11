# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def f(*args):
    # Note: np.broadcast rejects any **kwargs, even *{}
    exit(np.broadcast(args[:1]))

opts = converter.ConversionOptions(internal_convert_user_code=False)
self.assertIsNotNone(
    api.converted_call(f, (1, 2, 3, 4), None, options=opts))

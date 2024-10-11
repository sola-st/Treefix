# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
x = api.converted_call(range, (3,), None, options=DEFAULT_RECURSIVE)
self.assertEqual((0, 1, 2), tuple(x))

x = api.converted_call(
    re.compile, ('mnas_v4_a.*\\/.*(weights|kernel):0$',),
    None,
    options=DEFAULT_RECURSIVE)
self.assertIsNotNone(x.match('mnas_v4_a/weights:0'))

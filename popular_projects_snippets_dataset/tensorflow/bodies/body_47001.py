# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/test_util.py
dtype = self.dtype
if dtype in ('float16', 'bfloat16'):
    dtype = 'float32'
self.v = self.add_weight(
    'v', (),
    initializer='ones',
    dtype=dtype,
    experimental_autocast=False,
    regularizer=self._regularizer)
self.built = True

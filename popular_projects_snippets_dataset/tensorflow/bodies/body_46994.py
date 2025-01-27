# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/test_util.py
self._assert_type = (dtypes.as_dtype(assert_type).name if assert_type
                     else None)
super(AssertTypeLayer, self).__init__(**kwargs)

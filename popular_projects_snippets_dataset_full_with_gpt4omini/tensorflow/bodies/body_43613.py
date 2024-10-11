# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use_test.py
def get_shape(h):
    _ = h.shape
self._testAddShouldUseWarningWhenUsed(get_shape, name='blah_get_name')
gc.collect()
self.assertFalse(gc.garbage)

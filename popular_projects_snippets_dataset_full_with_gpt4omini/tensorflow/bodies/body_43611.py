# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use_test.py
def add(h):
    _ = h + 1
self._testAddShouldUseWarningWhenUsed(add, name='blah_add')
gc.collect()
self.assertFalse(gc.garbage)

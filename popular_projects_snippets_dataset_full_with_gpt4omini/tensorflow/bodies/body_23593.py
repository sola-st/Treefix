# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
class NotTrackable(object):
    pass

with self.assertRaises(ValueError):
    data_structures.List([NotTrackable()])

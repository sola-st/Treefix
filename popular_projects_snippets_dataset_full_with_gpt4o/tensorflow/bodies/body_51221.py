# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder_test.py

class NotEncodable(object):
    pass

self.assertFalse(nested_structure_coder.can_encode([NotEncodable()]))

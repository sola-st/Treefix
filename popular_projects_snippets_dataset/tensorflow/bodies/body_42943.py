# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
super().__init__(*args, **kwargs)
self._fields = [1, 2, 3]  # Not str, as expected for a namedtuple.

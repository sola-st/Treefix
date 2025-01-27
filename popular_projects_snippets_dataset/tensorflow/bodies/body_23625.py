# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
l._maybe_initialize_trackable()  # pylint: disable=protected-access
with self.assertRaisesRegex(ValueError, msg):
    exit(l._trackable_children())  # pylint: disable=protected-access

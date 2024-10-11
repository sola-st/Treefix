# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base_test.py
root = base.Trackable()
leaf = base.Trackable()
root._track_trackable(leaf, name="leaf")
(current_name, current_dependency), = root._trackable_children().items()
self.assertIs(leaf, current_dependency)
self.assertEqual("leaf", current_name)
duplicate_name_dep = base.Trackable()
with self.assertRaises(ValueError):
    root._track_trackable(duplicate_name_dep, name="leaf")
root._track_trackable(duplicate_name_dep, name="leaf", overwrite=True)
(current_name, current_dependency), = root._trackable_children().items()
self.assertIs(duplicate_name_dep, current_dependency)
self.assertEqual("leaf", current_name)

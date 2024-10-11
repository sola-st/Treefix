# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/autotrackable_test.py
root = autotrackable.AutoTrackable()
root.leaf = autotrackable.AutoTrackable()
root.leaf = root.leaf
duplicate_name_dep = autotrackable.AutoTrackable()
with self.assertRaisesRegex(ValueError, "already declared"):
    root._track_trackable(duplicate_name_dep, name="leaf")
# No error; we're overriding __setattr__, so we can't really stop people
# from doing this while maintaining backward compatibility.
root.leaf = duplicate_name_dep
root._track_trackable(duplicate_name_dep, name="leaf", overwrite=True)
self.assertIs(duplicate_name_dep, root._lookup_dependency("leaf"))
self.assertIs(duplicate_name_dep, root._trackable_children()["leaf"])

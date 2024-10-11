# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
root = autotrackable.AutoTrackable()
leaf = autotrackable.AutoTrackable()
# Dots are escaped, which avoids conflicts with reserved names.
root._track_trackable(leaf, name=".ATTRIBUTES")
trackable_utils.add_variable(trackable=leaf, name="a", shape=[])
checkpoint_key = _get_all_checkpoint_names(root)[0]
self.assertEqual("..ATTRIBUTES/a/.ATTRIBUTES/VARIABLE_VALUE",
                 checkpoint_key)
